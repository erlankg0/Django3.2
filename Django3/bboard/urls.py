from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .models import Bb
from .views import BbCreatView, BbUpdateView
from .views import high_index, BbDetailView, templateResponse_index, indexing, BbListView, BbAddView
from .views import index
from .views import low_index

urlpatterns = [
    path("", index, name='index'),
    path("<int:rubric_id>/", BbListView.as_view(), name='by_rubric'),
    path('add/', BbAddView.as_view(), name='add'),
    path('low/', low_index, name='low'),
    path('edit/<int:pk>', BbUpdateView.as_view(), name='update'),
    path('index/', high_index, name='high'),
    path('template/', templateResponse_index, name='template'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path("steam/", indexing),
    path("class/", BbCreatView.as_view(model=Bb, template_name='bboard/create.html', fields='title'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
