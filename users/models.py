from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    class theme(models.TextChoices):
        light = 'L', 'Light'
        dark = 'D', 'Dark'
    class language(models.TextChoices):
        RUSSIAN = 'russian', 'Russian'
        ENGLISH = 'english', 'English'
        UZB = 'uzb', 'Uzb'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notifications = models.BooleanField(default=True)
    interface_language = models.CharField(max_length=120, choices=language.choices, default=language.UZB)
    theme = models.CharField(max_length=20, choices=theme.choices, default=theme.light)

    def __str__(self):
        return f"{self.user.username}'s Settings"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)
    permanent_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class myPetition(models.Model):
    pass

class currentInstitute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)