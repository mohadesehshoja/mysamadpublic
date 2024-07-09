from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from apis.models.user import Admin
import datetime

import jwt

from apis.serializations.adminserialization import AdminSerializer
from module.check import Is_Find


class AdminViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Admin.objects.all()
        serializer = AdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        unis = request.data.get("unis")
        gettoken = Is_Find(Admin, username, password, unis)
        if gettoken:
            admin = Admin.objects.filter(password=password).first()
            admin_load = {
                'id': admin.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            admin_token = jwt.encode(admin_load, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='admin_token', value=admin_token, httponly=True)
            response.data = {
                'admin_token': str(admin_token)
            }
            return response
        else:
            return Response("you dont admin!!!")


class AdminLogoutViewSet(viewsets.ViewSet):
    def list(self, request):
        response = Response()
        response.delete_cookie(key='admin_token')
        response.data = {
            'message': 'logged out Admin'
        }
        return response
