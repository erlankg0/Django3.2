from django.urls import path
from .views import index, by_rubric
from .views import BbCreatView

urlpatterns = [
    path("", index, name='index'),
    path("<int:rubric_id>/", by_rubric, name='by_rubric'),
    path("add/", BbCreatView.as_view(), name="add"),
]
