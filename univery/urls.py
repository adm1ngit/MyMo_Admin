
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', InstituteFacultyRouteApi.as_view(), name='institute-list'),
    path('<int:pk>/', InstituteFacultyRouteApi.as_view()),
    path('faculties/', FacultyRouteListApi.as_view(), name='faculty-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

