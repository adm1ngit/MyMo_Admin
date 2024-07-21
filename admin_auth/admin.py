from django.contrib import admin
from .forms import RegisterForm
from .models import VideoEntry
class AdminRegisterForm(RegisterForm):
    list_display = ('email', 'password', 'password2')
    search_fields = ('email', 'password')

admin.site.register(VideoEntry)