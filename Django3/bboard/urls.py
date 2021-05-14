from django.urls import path
from .views import index, TemplateViews
from .views import BbCreatView, CreateView
from .views import add, add_save, add_and_save, low_index
from .views import high_index,BbDetailView, templateResponse_index, detail, indexing
from .models import Bb
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", index, name='index'),
    path("<int:rubric_id>/", TemplateViews.as_view(), name='by_rubric'),
    path('add/', add_and_save, name='add'),
    path('low/', low_index, name='low'),
    path('index/', high_index, name='high'),
    path('template/', templateResponse_index, name='template'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path("steam/", indexing),
    path("class/", BbCreatView.as_view(model=Bb, template_name='bboard/create.html', fields='title'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
