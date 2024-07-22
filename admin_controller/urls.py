from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VideoListCreateAPIView, VideoDetailAPIView, VideoDeleteAPIView

urlpatterns = [
    path("videos/", VideoListCreateAPIView.as_view(), name='video-list-create'),
    path("videos/<int:pk>/", VideoDetailAPIView.as_view(), name='video-detail'),
    path("videos/<int:pk>/delete/", VideoDeleteAPIView.as_view(), name='video-delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

