from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS = (
        ('Direktor', 'Direktor'),
        ('Admin', 'Admin'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='Admin')


# Create your models here.
