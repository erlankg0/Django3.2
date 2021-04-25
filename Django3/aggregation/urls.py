from django.urls import path
from .views import BookList, MyView

urlpatterns = [
    path("", BookList.as_view()),
    path("mine/", MyView.as_view(), name="my-view")
]
