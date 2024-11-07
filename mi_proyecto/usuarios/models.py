# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Puedes considerar usar hashed passwords

    def __str__(self):
        return self.username

class Specialist(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # También considera usar hashed passwords

    def __str__(self):
        return self.name

