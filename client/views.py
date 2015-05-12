from django.template.response import TemplateResponse
from django.views.generic import View
from django.conf import settings


class HomeView(View):

    def get(self, request):
        context = {
            "fb_id": settings.SOCIAL_AUTH_FACEBOOK_KEY,
        }

        return TemplateResponse(request, 'home.html', context)

# Create your views here.
