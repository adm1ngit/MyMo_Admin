from django.db import models

class VideoEntry(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  video = models.URLField()

  def __str__(self):
    return self.title



