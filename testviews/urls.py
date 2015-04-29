from django.views.generic import TemplateView
from django.conf.urls import patterns


urlpatterns = patterns('',
    (r'^test/social_login/$', TemplateView.as_view(template_name='social_login.html')),
)
