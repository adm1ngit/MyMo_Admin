from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Media(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
