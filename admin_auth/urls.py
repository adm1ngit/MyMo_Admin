from django.urls import path
from .views import RegisterView, LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = [
    path('media/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

