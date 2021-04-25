from django.shortcuts import render
from django.views.generic import ListView
from .models import Publisher


class PublisherList(ListView):
    model = Publisher
    context_object_name = "publishers"
# Create your views here.
