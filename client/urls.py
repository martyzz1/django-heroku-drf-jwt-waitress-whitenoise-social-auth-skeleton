from django.conf.urls import patterns, include, url
from testviews import urls as testviews_urls
from .views import HomeView
from django.conf import settings

urlpatterns = patterns('',
    url(r'', include(testviews_urls)),
    url(r'^$', HomeView.as_view(), name='home'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
