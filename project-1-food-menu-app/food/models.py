from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,
                                  default="https://dummyimage.com/600x400/000/fff.png")

    user_name = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  default=1)  # items that were already there, get user pk=1

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={"pk": self.pk})

