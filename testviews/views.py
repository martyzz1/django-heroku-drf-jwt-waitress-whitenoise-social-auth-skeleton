from django.template.response import TemplateResponse
from django.views.generic import View
from django.conf import settings


class TestSocialView(View):

    def get(self, request):
        context = {
            "fb_id": settings.SOCIAL_AUTH_FACEBOOK_KEY,
        }

        return TemplateResponse(request, 'social_login.html', context)
