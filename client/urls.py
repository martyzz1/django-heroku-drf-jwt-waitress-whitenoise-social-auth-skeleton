from django.conf.urls import patterns, include, url
from testviews import urls as testviews_urls
from .views import HomeView
from django.conf import settings


client_urls = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'', include(testviews_urls)),
)

urlpatterns = patterns('',
    url(r'', include(client_urls, namespace='client')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
