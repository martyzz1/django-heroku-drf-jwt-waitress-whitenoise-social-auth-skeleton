from .serializers import UserSerializer
from django.conf import settings
from datetime import datetime


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }


def jwt_payload_handler(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    exp = datetime.utcnow() + settings.JWT_CLIENT_REFRESH_EXPIRATION_DELTA

    if user.is_provider():
        exp = datetime.utcnow() + settings.JWT_PROVIDER_REFRESH_EXPIRATION_DELTA

    payload = {
        'user_id': user.pk,
        'email': user.email,
        'username': username,
        'exp': exp
    }
    print payload
    print exp
    return payload
