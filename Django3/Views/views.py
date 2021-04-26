from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book


class PublisherList(ListView):
    model = Publisher
    context_object_name = "publishers"


class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'Views/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class PublisherDetailOne(DetailView):
    context_object_name = "publisherOne"
    template_name = "Views/detailOne.html"
    queryset = Publisher.objects.all()


class BookList(ListView):
    queryset = Book.objects.order_by("title")
    context_object_name = "book_list"
    template_name = "Views/list_book.html"
# Create your views here.
