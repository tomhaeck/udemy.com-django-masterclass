from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)

    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()

    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(to=User,
                                on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(to=Food,
                                      on_delete=models.CASCADE)
    # this is actually a connection model that models a many-to-many relationship
    # between users and foods

