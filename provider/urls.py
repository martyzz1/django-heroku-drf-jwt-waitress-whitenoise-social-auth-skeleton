from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import HomeView

provider_urls = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
)

urlpatterns = patterns('',
    url(r'', include(provider_urls, namespace='client')),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
