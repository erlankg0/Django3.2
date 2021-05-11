from django.urls import path
from .views import index, by_rubric
from .views import BbCreatView
from .views import add, add_save, add_and_save, low_index
from .views import high_index, templateResponse_index
urlpatterns = [
    path("", index, name='index'),
    path("<int:rubric_id>/", by_rubric, name='by_rubric'),
    path('add/', add_and_save, name='add'),
    path('low/', low_index, name='low'),
    path('index/', high_index, name='high'),
    path('template/', templateResponse_index, name='template' )
]
