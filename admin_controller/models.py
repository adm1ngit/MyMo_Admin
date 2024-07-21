from django.db import models
class VideoApp(models.Model):
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    marked_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - {self.name}"

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ('created_at',)
