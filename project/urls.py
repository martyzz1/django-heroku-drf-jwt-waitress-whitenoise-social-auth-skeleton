from django.conf.urls import patterns, include, url
from django.conf import settings
from subdomains.utils import reverse
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^.*$', RedirectView.as_view(url=reverse('client:home', subdomain='client'), permanent=False))
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
