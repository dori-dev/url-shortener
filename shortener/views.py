from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Url
from .utils import generate_uuid


def index(request: WSGIRequest):
    """index page of url shortener website
    """
    return render(request, 'index.html')


def create(request: WSGIRequest):
    """"""
    if request.method == "POST":
        link = request.POST['link']
        uuid = generate_uuid()
        new_url = Url(link=link, uuid=uuid)
        new_url.save()
        return HttpResponse(uuid)
    return HttpResponse("Nothings Here")
