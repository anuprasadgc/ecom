from django.db import models

# Create your models here.

class Products(models.Model):

    #def __self__(self):
        #return self.title
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=500)
    original_price = models.FloatField()
    discound_price = models.FloatField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)