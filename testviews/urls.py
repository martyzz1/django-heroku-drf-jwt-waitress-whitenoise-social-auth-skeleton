from views import TestSocialView
from django.conf.urls import patterns


urlpatterns = patterns('',
    (r'^test/social_login/$', TestSocialView.as_view()),
)
