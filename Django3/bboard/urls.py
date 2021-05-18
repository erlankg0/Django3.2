from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .models import Bb
from .views import (Index, BbCreatView, BbUpdateView, BbDeleteView, BbDetailView, BbByRubricView)
from .views import (MonthViews, BbAddView, YearIndexView)

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path('archive/<slug:year>/', YearIndexView.as_view(), name='year'),
    path('month/<slug:year>/<slug:month>/', MonthViews.as_view(), name='month'),
    path("<int:rubric_id>/", BbByRubricView.as_view(), name='by_rubric'),
    path('add/', BbAddView.as_view(), name='add'),
    path('edit/<int:pk>/', BbUpdateView.as_view(), name='update'),
    path("delet/<int:pk>/", BbDeleteView.as_view(), name="delete"),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
