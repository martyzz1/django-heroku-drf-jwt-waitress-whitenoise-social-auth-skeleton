from django.conf.urls import patterns, include, url
from django.contrib import admin
from testviews import urls as testviews_urls
from users import urls as users_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(testviews_urls)),
    url(r'^', include(users_urls)),
)
