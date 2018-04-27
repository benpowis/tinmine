from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Drink(models.Model):
    drink_name = models.CharField(max_length=100)
    drink_desc = models.CharField(max_length=250, default='...')
    strength = models.IntegerField(default=0)
    price = models.IntegerField(default=1)
    def __str__(self):
        return self.drink_name


class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    health = models.IntegerField(default=100)
    strength = models.IntegerField(default=50)
    charisma = models.IntegerField(default=50)
