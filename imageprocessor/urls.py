from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.image_process, name='image_process'),
]