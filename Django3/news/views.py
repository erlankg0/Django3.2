from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all()
    res = "<h1>Список новостей</h1>"
    for item in news:
        res += f"<div><p>{item.title}</p>" \
               f"<p>{item.content}</p></div>"
    return HttpResponse(res)