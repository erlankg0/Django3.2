from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    context = {"News": news}
    return render(request, template_name='news/index.html', context=context)
