from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse(f"{request} Hello word!")
