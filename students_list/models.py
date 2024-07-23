from django.db import models

# Create your models here.

class Students(models.Model):
    photo = models.ImageField(upload_to = 'students/')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    paycom = models.CharField(max_length=100)
    education_stage = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    education_status = models.CharField(max_length=100)
    education_form = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    jshshir = models.CharField(max_length=100)
