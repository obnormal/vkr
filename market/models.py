from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def add_position(self):
        pass

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_day = models.DateField(default=None)
    wallet_id = models.CharField(max_length=50)
