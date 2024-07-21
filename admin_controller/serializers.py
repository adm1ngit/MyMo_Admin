from .models import VideoApp
from rest_framework import serializers
class VideoAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoApp
        fields = '__all__'