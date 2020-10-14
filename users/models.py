# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null=True, blank=True)
	nickname = models.CharField(max_length=100, null=False)