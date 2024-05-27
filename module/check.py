import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from apis.models.user import MyUser, Admin


def CheckAuthentication(token):
    user_check = True
    if not token:
        user_check = False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        user_check = False
    try:
        user = MyUser.objects.get(pk=payload['id'])
    except UnboundLocalError:
        user_check = False
    if user_check:
        return user
    return user_check


def CheckToken(token):
    admin_check = True
    if not token:
        admin_check = False
    try:
        admin_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        admin_check = False
    try:
        admin = Admin.objects.get(pk=admin_token['id'])
    except UnboundLocalError:
        admin_check = False
    if admin_check:
        return admin
    return admin_check
