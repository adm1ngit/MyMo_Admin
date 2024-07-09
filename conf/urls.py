from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin_auth/next/page/", include("admin_auth.urls")),
    # path("admin_controller/", include("admin_controller.urls")),
]
