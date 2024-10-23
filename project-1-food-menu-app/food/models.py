from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,
                                  default="https://dummyimage.com/600x400/000/fff.png")

    def __str__(self):
        return self.item_name

