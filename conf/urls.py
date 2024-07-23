from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("controller/", include("admin_controller.urls")),
    path("admin_auth/next/page/", include("admin_auth.urls")),
    path("users/", include("users.urls")),
    path("univery/", include("univery.urls")),
    path("students/list/", include("students_list.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)