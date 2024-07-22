from django.db import models


class Institute(models.Model):
    logo = models.ImageField(upload_to='logo/')
    name = models.CharField(max_length=255)
    description = models.TextField(520)
    website = models.URLField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    address = models.CharField(max_length=255)
    grand = models.IntegerField(null=True, blank=True)
    contract = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    facultetyName = models.CharField(max_length=255)

    def __str__(self):
        return self.facultetyName


class FacultyRoute(models.Model):
    class routeType(models.TextChoices):
        BAKALAVR = 'bakalavr', 'Bakalavr'
        MAGISTRATURA = 'magistratura', 'Magistratura'

    class language(models.TextChoices):
        RUSSIAN = 'russian', 'Russian'
        ENGLISH = 'english', 'English'
        UZB = 'uzb', 'Uzb'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    routeCode = models.CharField(max_length=255, null=True, blank=True)
    routeName = models.CharField(max_length=255)
    routeType = models.CharField(max_length=120, choices=routeType.choices, default=routeType.BAKALAVR)
    daySum = models.IntegerField(null=True, blank=True)
    nightSum = models.IntegerField(null=True, blank=True)
    sirtqiSum = models.IntegerField(null=True, blank=True)
    dayKvota = models.IntegerField(null=True, blank=True)
    nightKvota = models.IntegerField(null=True, blank=True)
    sirtqiKvota = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=120, choices=language.choices, default=language.UZB)

    def __str__(self):
        return self.routeName
