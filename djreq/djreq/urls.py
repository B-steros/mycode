#!/usr/bin/python3

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
        path('astro/', views.astro),
        path('nasa/', views.nasa),
        ]
