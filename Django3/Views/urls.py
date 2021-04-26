from django.urls import path
from .views import PublisherList, PublisherDetail, PublisherDetailOne, BookList
from .views import AcmeBookList

urlpatterns = [
    path("", PublisherList.as_view()),
    path("detail/<int:pk>", PublisherDetail.as_view()),
    path("details/<int:pk>", PublisherDetailOne.as_view()),
    path("book/", BookList.as_view()),
    path("acme/<publisher>", AcmeBookList.as_view())
]
