# Create your views here.
from django.http import Http404, HttpResponse

from AProject.settings import SITE_TITLE


def hello(request):
    return  HttpResponse(SITE_TITLE)