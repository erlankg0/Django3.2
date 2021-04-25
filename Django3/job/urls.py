from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("find/", job),
    path("find/<int:pk>/", my_view),
    path("about/", AboutView.as_view()),
]
