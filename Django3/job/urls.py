from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("<str:name>/<str:surname>/<slug:slug>/", year)
]
