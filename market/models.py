from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
from untitled import settings


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        pass


class Order(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODELS, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    odrder_dates = models.DateTimeField()
    ordered = models.BooleanField(default=False)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_day = models.DateField(default=None)
    wallet_id = models.CharField(max_length=50)
