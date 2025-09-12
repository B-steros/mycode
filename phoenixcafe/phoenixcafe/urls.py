#!/usr/bin/python5

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('sleepy/', views.sleepy),
    path('clock/', views.current_datetime),
]
#urlpatterns += [path('clock/', views.current_datetime),]
