from django.urls import path
from .views import MediaListCreateView, MediaDetailView

urlpatterns = [
    path('media/', MediaListCreateView.as_view(), name='media-list-create'),
    path('media/<int:pk>/', MediaDetailView.as_view(), name='media-detail'),
]
