from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()

    # better practice to store your images as URLs
    # that are hosted on a different server,
    # so no ImageField
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Order(models.Model):
    items = models.CharField(max_length=1000)

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    total = models.CharField(max_length=200)