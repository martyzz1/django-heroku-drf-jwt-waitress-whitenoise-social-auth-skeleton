# -*- coding: utf-8 -*-
"""
Django settings for Pawz API project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from configurations import Configuration, values

BASE_DIR = dirname(dirname(__file__))


class Common(Configuration):

    # APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'oauth2_provider',  # for oauth2 server
        'rest_framework',  # for build RESTFull API
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'users',  # custom users app
        # Your stuff: custom apps go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    INSTALLED_APPS += (
        # Needs to come last for now because of a weird edge case between
        # 'allauth',  # registration
        # 'allauth.account',  # registration
        # 'allauth.socialaccount',  # registration
    )
    # END APP CONFIGURATION

    # MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = "CHANGEME!!!!"
    # END SECRET CONFIGURATION

    # FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    # END FIXTURE CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('tech', 'tech@project.couk'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    # https://django-configurations.readthedocs.org/en/0.5/values/#configurations.values.DatabaseURLValue
    DATABASES = values.DatabaseURLValue('postgres://localhost/api')
    # DATABASES['default']['ENGINE'] = 'django_postgrespool'
    # END DATABASE CONFIGURATION

    # CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify (used on heroku) is painful to install on windows.
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }
    # END CACHING

    # GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'UTC'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-gb'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    # END GENERAL CONFIGURATION

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        # "allauth.account.context_processors.account",
        # "allauth.socialaccount.context_processors.socialaccount",
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    # CRISPY_TEMPLATE_PACK = 'bootstrap3'
    # END TEMPLATE CONFIGURATION

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    # MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    # MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = 'project.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        # "allauth.account.auth_backends.AuthenticationBackend",
    )

    # Some really nice defaults
    # ACCOUNT_AUTHENTICATION_METHOD = "email"
    # ACCOUNT_EMAIL_REQUIRED = True
    # ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    # END AUTHENTICATION CONFIGURATION

    # Custom user app defaults
    # Select the correct user model
    # AUTH_USER_MODEL = "users.User"
    LOGIN_REDIRECT_URL = "/"
    LOGIN_URL = "account_login"
    # END Custom user app defaults

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    # END LOGGING CONFIGURATION

    # django-rest-framework CONFIGURATION
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }
    # END django-rest-framework CONFIGURATION

    # django-oauth-toolkit CONFIGURATION
    OAUTH2_PROVIDER = {
        # this is the list of available scopes
        'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
    }
    # END django-oauth-toolkit CONFIGURATION

    # Your common stuff: Below this line define 3rd party libary settings
