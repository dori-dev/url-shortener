from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    """index page of url shortener website
    """
    return render(request, 'index.html')


def create(request: WSGIRequest):
    pass
