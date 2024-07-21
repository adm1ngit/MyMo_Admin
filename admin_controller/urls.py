from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VideoListCreateAPIView

urlpatterns = [
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

