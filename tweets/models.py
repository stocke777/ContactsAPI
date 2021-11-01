from django.db import models

# Create your models here.
class Tweet(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()