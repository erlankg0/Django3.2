from django.shortcuts import render
from django.http import HttpResponse
import datetime

def year(request,name, surname, slug):
    date = datetime.datetime
    html = f"<h1>{date} {name} {surname} {slug}</h1>"
    return HttpResponse(html)



def index(request):
    now = datetime.datetime.now()
    html = f"<h1>{now}</h1>"
    return HttpResponse(html)
# Create your views here.
