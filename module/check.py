import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from apis.models.user import User


def CheckAuthentication(token):
    if not token:
        return AuthenticationFailed('Token is missing')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return AuthenticationFailed('Token is missing')
    try:
        user = User.objects.get(pk=payload['id'])
    except user.DoesNotExist:
        return Response("Unis does not exist")
    return user
