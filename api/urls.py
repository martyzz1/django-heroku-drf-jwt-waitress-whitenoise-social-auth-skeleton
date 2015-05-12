from django.conf.urls import patterns, include, url
from users import urls as users_urls
from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include(users_urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
