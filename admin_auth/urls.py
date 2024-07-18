from .views import RegisterView, LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoEntryView

urlpatterns = [
    path("videos/", VideoEntryView.as_view()),
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
]

