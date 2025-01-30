from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username