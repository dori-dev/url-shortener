"""shortener views
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from .models import Url
from .utils import generate_uuid


def index(request: WSGIRequest):
    """index page of url shortener website
    """
    return render(request, 'index.html')


def create(request: WSGIRequest):
    """create url page for ajax
    """
    if request.method == "POST":
        link = request.POST['link']
        uuid = generate_uuid()
        new_url = Url(link=link, uuid=uuid)
        new_url.save()
        return HttpResponse(uuid)
    return HttpResponse("Nothings Here")


def url(request: WSGIRequest, url_id: str):
    """url view

    Args:
        url_id (str): id of url

    Returns:
        redirect to url link
    """
    url_details: QuerySet[Url] = Url.objects.filter(uuid=url_id)
    if url_details.exists():
        return redirect(url_details[0].link)
    return redirect("index")
