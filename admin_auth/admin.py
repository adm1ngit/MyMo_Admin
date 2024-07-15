from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', "password", "confirm_password")
    search_fields = ('email', 'password')

