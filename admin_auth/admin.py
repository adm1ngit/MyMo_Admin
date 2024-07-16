from django.contrib import admin

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', "password", "password2")
    search_fields = ('email', 'password')
