from django.urls import path
from admin_controller import views

urlpatterns = [
    path("videos/", views.VideoAppView.as_view()),
]
