from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    image_url = models.CharField(max_length=500, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self):
        return f"{self.owner}: {self.title}"

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass