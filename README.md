# django-heroku-drf-waitress-whitenoise-skeleton
Got tired of trying to setup latest best practice Django  - so built my own... 

Covers the following scenario:-

Pure API Server, allowing signup & Login via manual username/email & password  or by sending a social account access token.
Designed so that Web or mobile clients may use native Social Auth. 

It is my intention this project will also provide Multiple User types at some point.


* django
* celery
* Honcho
* heroku optimised
* django-rest-framework
* waitress webserver (not gunicorn)
* whitenoise for static files
* python-social-auth for Social Authentication
* django-rest-framework-jwt
* django-configurations

You will need to setup the following Envrionment variables
<pre>
export DJANGO_SETTINGS_MODULE=project.settings.local
export DJANGO_CONFIGURATION=Local
export DATABASE_URL=postgres://user:pass@yourhost/dbname
export DJANGO_BROKER_URL=amqp://user:pass@yourhost:5672/vhost
export DJANGO_SECRET_KEY=<set your own>
export DJANGO_SOCIAL_AUTH_FACEBOOK_KEY=<your key>
export DJANGO_SOCIAL_AUTH_FACEBOOK_SECRET=<your secret>
</pre>

You may use see a working proof that everything is working as it should y navigating to the following url:-

http://localhost:8000/test/social_login/


*Inspiration*
* http://httplambda.com/a-rest-api-with-django-and-oauthw-authentication/
* http://blog.wizer.fr/2013/11/angularjs-facebook-with-a-django-rest-api/
* http://bytefilia.com/titanium-mobile-facebook-application-django-allauth-sign-sign/
* https://github.com/luzfcb/cookiecutter-django-oauth
* http://stackoverflow.com/questions/22198724/duplicate-email-using-both-python-social-auth-and-email-registration-in-django
