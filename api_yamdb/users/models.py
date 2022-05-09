from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    roles = ()
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    role = models.CharField(
        max_length=150,
        blank=True
    )
    bio = models.TextField()
    def __str__(self):
        return str(self.username)