from django.urls import path
from .views import *

urlpatterns = [
    path("settings/", UserSettingsView.as_view(), name='user-settings'),
    path("profile/", UserProfileAPIView.as_view(), name='user-profile'),
    path('user-pettions/', myPettionListCreateAPIView.as_view(), name='user-institutes'),

]