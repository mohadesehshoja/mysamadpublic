import datetime

import jwt

from rest_framework import viewsets, status
from rest_framework.response import Response
from apis.models.financial import Financial
from apis.models.reservation import Reservation
from apis.models.restaurant import MenuItem
from apis.models.university import University
from apis.models.user import User
from apis.serializations.userserialization import UserSerializer, UserLoginSerializer, UniversitySerializer, \
    ProfileSerializer, FinancialSerializer, ReservationSerializer
from module.check import CheckAuthentication


class UniversityViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LoginViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserLoginSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        gettoken = False
        username = request.data.get("username")
        password = request.data.get("password")
        unis = request.data.get("unis")
        qs = User.objects.filter(username=username)
        if qs.exists():
            ps = qs.filter(password=password)
            if ps.exists():
                my_uni = qs.filter(unis_id=unis)
                if my_uni.exists():
                    my_id = qs.first().id
                    gettoken = True

        if gettoken:
            payload = {
                'id': my_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='token', value=token, httponly=True)
            response.data = {
                'token': str(token)
            }
            return response
        else:
            return Response("first register")


class LogoutViewSet(viewsets.ViewSet):
    def list(self, request):
        response = Response()
        response.delete_cookie(key='token')
        response.data = {
            'message': 'logged out'
        }
        return response


class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)

    def create(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        data = request.data
        data.update({'user': user.id})
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinancialViewSet(viewsets.ViewSet):
    def list(self, request):
        final = []
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        for financial in Financial.objects.filter(user_id=user.id):
            data = {
                "id": financial.id,
                "created": financial.created,
                "modified": financial.modified,
                "active": financial.active,
                "payment_amount": financial.payment_amount,
                "payment_date": financial.payment_date,
                "payment_id": financial.payment_id,
                "user": user.id
            }
            final.append(data)
        return Response(final)

    def create(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        data = request.data
        data.update({'user': user.id})
        serializer = FinancialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        final = []
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        for reservation in Reservation.objects.filter(user_id=user.id):
            data = {
                "id": reservation.id,
                "created": reservation.created,
                "modified": reservation.modified,
                "active": reservation.active,
                "payment_amount": reservation.payment_amount,
                "payment_date": reservation.payment_date,
                "payment_id": reservation.payment_id,
                "menuitem": reservation.menuitem.id,
                "user": user.id
            }
            final.append(data)
        return Response(final)

    def create(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        data = request.data
        menuitem = MenuItem.objects.filter(id=data['menuitem'])
        data.update({'user': user.id})
        price = menuitem[0].meal.price
        data.update({"payment_amount": price})
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
