from django.conf.urls.static import static
from django.urls import path

from conf import settings
from .views import MediaListCreateView, MediaDetailView

urlpatterns = [
    path('media/', MediaListCreateView.as_view(), name='media-list-create'),
    path('media/<int:pk>/', MediaDetailView.as_view(), name='media-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
