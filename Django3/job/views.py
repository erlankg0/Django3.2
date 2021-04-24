from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime


def year(request, name, surname, slug):
    date = datetime.date
    html = f"<h1>{date} {name} {surname} {slug}</h1>"
    return HttpResponse(html)


def index(request):
    now = datetime.datetime.now()
    html = f"<h1>{now}</h1>"
    return HttpResponse(html)
