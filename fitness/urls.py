from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("Home/", views.hello_jake),
]
