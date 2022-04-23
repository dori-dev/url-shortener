"""shortener urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<str:url_id>/', views.url, name="url")
]
