# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('tenant', 'Tenant'),
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tenant')

    def __str__(self):
        return f"{self.username} ({self.role})"
