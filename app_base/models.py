from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=500)
    original_price = models.FloatField()
    discound_price = models.FloatField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
