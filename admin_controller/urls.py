from django.urls import path
from .views import VideoListCreateAPIView

urlpatterns = [
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
]

