import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from apis.models.user import MyUser, Admin


def CheckAuthentication(token):
    if not token:
        return False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return False
    try:
        user = MyUser.objects.get(pk=payload['id'])
        return user
    except UnboundLocalError:
        return False


def CheckToken(token):
    if not token:
        return False
    try:
        admin_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return False
    try:
        admin = Admin.objects.get(pk=admin_token['id'])
        return admin
    except UnboundLocalError:
        return False


def Is_Find(model, username, password, unis):
    qs = model.objects.filter(username=username)
    if qs.exists():
        ps = qs.filter(password=password)
        if ps.exists():
            my_uni = qs.filter(unis_id=unis)
            if my_uni.exists():
                return True
            return False
        return False
    return False
