web: waitress-serve --port=$PORT project.wsgi:application
celery_default_queue: env CELERY_HOSTNAME=celery_default_queue celery worker --app=project.celery --loglevel=DEBUG -n celery_default_queue --queues celery_default_queue --concurrency=1
~

