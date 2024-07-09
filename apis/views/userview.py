import datetime

import jwt

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from apis.models.financial import Financial
from apis.models.reservation import Reservation
from apis.models.restaurant import MenuItem
from apis.models.university import University
from apis.models.user import MyUser
from apis.serializations.userserialization import UserSerializer, UniversitySerializer, \
    ProfileSerializer, FinancialSerializer, ReservationSerializer, UserLoginSerializer
from module.check import CheckAuthentication, CheckToken, Is_Find


class UniversityViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            queryset = MyUser.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response("you must be admin!!")

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin!!")


class LoginViewSet(generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserLoginSerializer

    def get(self, request):
        queryset = MyUser.objects.all()
        serializer = UserLoginSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        unis = request.data.get("unis")
        gettoken = Is_Find(MyUser, username, password, unis)
        if gettoken:
            user = MyUser.objects.filter(password=password).first()
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            user_token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='user_token', value=user_token, httponly=True)
            response.data = {
                'user_token': str(user_token)
            }
            return response
        else:
            return Response("first register")


class LogoutViewSet(viewsets.ViewSet):
    def list(self, request):
        response = Response()
        response.delete_cookie(key='user_token')
        response.data = {
            'message': 'logged out'
        }
        return response


class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)

    def create(self, request):
        token = request.COOKIES.get('user_token')
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
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        queryset = Financial.objects.filter(user=user)
        serializer = FinancialSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        data = request.data
        data.update({'user': user.id})
        serializer = FinancialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            myself = MyUser.objects.get(id=user.id)
            MyUser.charge_amount(myself, serializer.data["payment_amount"])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        queryset = Reservation.objects.filter(user=user)
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        data = request.data
        menuitem = MenuItem.objects.filter(id=data['menuitem'])
        data.update({'user': user.id})
        price = menuitem[0].meal.price
        data.update({"payment_amount": price})
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            myself = MyUser.objects.get(id=user.id)
            MyUser.spend_amount(myself, serializer.data["payment_amount"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
