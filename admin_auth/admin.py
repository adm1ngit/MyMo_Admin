from django.contrib import admin
from .forms import RegisterForm

class AdminRegisterForm(RegisterForm):
    list_display = ('email', 'password', 'password2')
    search_fields = ('email', 'password')
