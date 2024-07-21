from django.contrib import admin
from .models import VideoApp

class VideoAppAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name", "description")
    list_filter = ("name",)

admin.site.register(VideoApp, VideoAppAdmin)