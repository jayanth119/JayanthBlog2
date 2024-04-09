# models.py

from django.db import models

class Icon(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100 ,  default='Untitled' )
    description = models.TextField()
    icons = models.ManyToManyField(Icon)
    image = models.ImageField(upload_to='static/')
    link = models.URLField()

    def __str__(self):
        return self.title
