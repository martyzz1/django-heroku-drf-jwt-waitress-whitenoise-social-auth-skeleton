# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use sendgird to sendemails
- Use MEMCACHIER on Heroku
'''
from configurations import values
from project.settings.common import Common


class Production(Common):

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # SECRET KEY
    SECRET_KEY = values.SecretValue()
    # END SECRET KEY

    # django-secure
    INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = [
        "client.pawz.co.uk",
        "provider.pawz.co.uk",
        "api.pawz.co.uk",
        "admin.pawz.co.uk",
    ]
    # END SITE CONFIGURATION

    SUBDOMAIN_URLCONFS = {
        None: 'project.urls',  # no subdomain, e.g. ``example.com``
        'client': 'client.urls',
        'provider': 'provider.urls',
        'api': 'api.urls',
        'admin': 'admin.urls',
    }

    # INSTALLED_APPS += ("", )

    # STORAGE CONFIGURATION
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += (
        # 'storages',
    )

    # EMAIL
    DEFAULT_FROM_EMAIL = values.Value('Pawz API <noreply@api.pawz.co.uk>')
    EMAIL_HOST = values.Value('smtp.sendgrid.com')
    EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
    EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
    EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    EMAIL_SUBJECT_PREFIX = values.Value('[Pawz API] ', environ_name="EMAIL_SUBJECT_PREFIX")
    EMAIL_USE_TLS = True
    SERVER_EMAIL = EMAIL_HOST_USER
    # END EMAIL

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    # END TEMPLATE CONFIGURATION

    # CACHING
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify is painful to install on windows.
    try:
        # See: https://github.com/rdegges/django-heroku-memcacheify
        from memcacheify import memcacheify
        CACHES = memcacheify()
    except ImportError:
        CACHES = values.CacheURLValue(default="memcached://127.0.0.1:11211")
    # END CACHING

    # Your production stuff: Below this line define 3rd party libary settings
