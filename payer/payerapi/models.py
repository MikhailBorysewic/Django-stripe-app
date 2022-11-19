from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, id {self.id}"


class Discount(models.Model):
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.size}, id {self.id}%"


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="items")
    discount = models.OneToOneField(Discount, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Order, id {self.id}"
