from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

# https://github.com/jezdez/django-configurations/issues/101
from configurations import importer
importer.install()


app = Celery('project')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
