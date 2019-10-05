from django.db import models

# Create your models here.
class Twit (models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField('twits')

