#!/usr/bin/python3

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

def ierror(request):
    return HttpResponseNotFound("Page was not found")

def success(request):
    return HttpResponse("Page was found")

def customheader(request):
    x = {}
    x['learning'] = 'Django'
    x['speed'] = 55

    return HttpResponse(headers=x)

def customcode(request):
    return HttpResponse("Working on that", status=201)
