# from django.http import HttpResponse
# from django.contrib.auth import login
from social.apps.django_app.utils import psa
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.conf import settings
from calendar import timegm
from datetime import datetime


# When we send a third party access token to that view
# as a GET request with access_token parameter,
# python social auth communicate with
# the third party and request the user info to register or
# sign in the user. Magic. Yeah.


# @psa('social:complete')
@psa()
def auth_by_token(request, backend):
    """Decorator that creates/authenticates a user with an access_token"""
    # token = request.DATA.get('access_token')
    user = request.user
    user = request.backend.do_auth(
        access_token=request.DATA.get('access_token')
    )
    if user:
        return user
    else:
        return None


class SocialTokentoJWT(APIView):
    """View to authenticate users via a Social 3rd party access_token."""

    permission_classes = (permissions.AllowAny,)

    def post(self, request, backend):
        auth_token = request.DATA.get('access_token', None)
        if auth_token and backend:
            try:
                # Try to authenticate the user using python-social-auth
                user = auth_by_token(request, backend)
            except Exception, e:  # noqa
                return Response({
                    'status': 'Bad request',
                    'message': 'Could not authenticate with the provided token.'
                }, status=status.HTTP_400_BAD_REQUEST)
            if user:
                if not user.is_active:
                    return Response({
                        'status': 'Unauthorized',
                        'message': 'The user account is disabled.'
                    }, status=status.HTTP_401_UNAUTHORIZED)

                # This is the part that differs from the normal python-social-auth implementation.
                # Return the JWT instead.

                # Get the JWT payload for the user.
                payload = jwt_payload_handler(user)

                # Include original issued at time for a brand new token,
                # to allow token refresh
                if settings.JWT_ALLOW_REFRESH:
                    payload['orig_iat'] = timegm(
                        datetime.utcnow().utctimetuple()
                    )

                # Create the response object with the JWT payload.
                response_data = {
                    'token': jwt_encode_handler(payload)
                }

                return Response(response_data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Authentication could not be performed with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)
