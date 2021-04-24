from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from .models import Blog, Author, Entry
from django.template import loader


def year(request, name, surname, slug):
    date = datetime.date
    html = f"<h1>{date} {name} {surname} {slug}</h1>"
    return HttpResponse(html)


def index(request):
    now = datetime.datetime.now()
    html = f"<h1>{now}</h1>"
    return HttpResponse(html)


def job(request):
    blog = Blog.objects.all()
    author = Author.objects.all()
    entry = Entry.objects.all()
    context = {'blog': blog, "author": author, "entry": entry}
    return render(request, "job/job.html", context)


def my_view(request, pk):
    try:
        obj = Entry.objects.get(pk=pk)
        context = {"entry": obj}
        return render(request, "job/blog.html", context)
    except Entry.DoesNotExist:
        raise Http404("Ни одна Entry не соответствует данному запросу")
