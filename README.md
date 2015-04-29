# django-heroku-drf-waitress-whitenoise-skeleton
Got tired of trying to setup latest best practice Django  - so built my own... 

Covers the following scenario:-

Pure API Server, allowing signup & Login via manual username/email & password  or by sending a social account access token.
Designed so that Web or mobile clients may use native Social Auth. 

It is my intention this project will also provide Multiple User types at some point.


* django
* heroku optimised
* django-rest-framework
* waitress webserver (not gunicorn)
* whitenoise for static files
* django-allauth for Social Authentication
* django-rest-framework-jwt
* django-configurations



*Inspiration*
http://httplambda.com/a-rest-api-with-django-and-oauthw-authentication/
http://blog.wizer.fr/2013/11/angularjs-facebook-with-a-django-rest-api/
http://bytefilia.com/titanium-mobile-facebook-application-django-allauth-sign-sign/

