from django.urls import path
from .views import StudentsView
urlpatterns = [
    path("students/get/", StudentsView.as_view(), name="students"),
    path("students/post/", StudentsView.as_view(), name="students"),
]