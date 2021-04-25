from django.urls import path
from .views import BookList, MyView, my_views

urlpatterns = [
    path("", BookList.as_view()),
    path("mine/", MyView.as_view(), name="my-view"),
    path("authors/", my_views),
]
