from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Publisher, Book, Author
from django.shortcuts import get_object_or_404


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
    queryset = Book.objects.all()
    context_object_name = "book_list"
    template_name = "Views/list_book.html"


# Create your views here.

class AcmeBookList(ListView):
    template_name = "Views/acme_list.html"

    def get_queryset(self):
        self.publisher = get_object_or_404(PublisherList, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context

