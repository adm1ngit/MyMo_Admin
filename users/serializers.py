from rest_framework import serializers
from .models import *

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['notifications', 'interface_language', 'theme']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_picture', 'gender', 'birth_date', 'nationality', 'ethnicity', 'permanent_address', 'phone_number']