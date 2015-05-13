from views import TestSocialView
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^test/social_login/$', TestSocialView.as_view(), name='social_login'),
)
