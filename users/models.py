from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
