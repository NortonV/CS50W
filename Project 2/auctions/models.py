from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    picture = models.ImageField()

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass