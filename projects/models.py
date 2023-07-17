from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    skills = models.CharField(max_length=500, default='n/a')
    image_url = models.CharField(max_length = 2083)
    project_url = models.CharField(max_length = 2083)
