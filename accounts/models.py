import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    hackathon_participant = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='media/users', default='media/users/avatar.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
