from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)