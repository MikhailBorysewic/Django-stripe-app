from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    size = models.IntegerField()

