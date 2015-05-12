from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
