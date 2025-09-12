#!/usr/bin/python3

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
        path('ierror/', views.ierror),
        path('success/', views.success),
        path('header/', views.customheader),
        path('created/', views.customcode),
        ]

