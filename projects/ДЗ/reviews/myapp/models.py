from django.db import models

# Create your models here.

class Reviews(models.Model):
    username = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    