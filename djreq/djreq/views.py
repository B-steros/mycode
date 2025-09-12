#!/usr/bin/python3

import requests

from django.http import JsonResponse


API = "http://api.open-notify.org/astros.json"

APINASA = "https://api.nasa.gov/planetary/apod?api_key="

APIKEY = "DEMO_KEY"

def astro(request):
    res = requests.get(API)
    return JsonResponse(res.json())

def nasa(request):
    res = requests.get(f"{APINASA}{APIKEY}")
    return JsonResponse(res.json())

