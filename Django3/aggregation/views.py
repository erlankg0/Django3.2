from django.shortcuts import render
from .models import Author, Store, Publisher, Book
from django.views.generic import ListView
from django.http import HttpResponse
from django.views import View


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello, World!</h1>")


class BookList(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("pubdate")
        response = HttpResponse(
            headers={'Last-Modified': last_book.pubdate.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response
# Create your views here.
