from django.urls import path
from .views import LoginView

urlpatterns = [
    # path("level/forum/admin/page/register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
]
