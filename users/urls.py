from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    # the view to register our user with a third party token
    # the backend is the python social auth backend e.g. facebook
    url(r'^api/v1/auth/token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/auth/social/(?P<backend>[^/]+)/$', views.SocialTokentoJWT.as_view()),

)
