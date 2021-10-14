from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    api_key = models.CharField(blank=True, max_length=100)
    secret_key = models.CharField(blank=True, max_length=100)
    profile = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d")
    is_trading = models.BooleanField(default=False)


class Profile(models.Model):
    pass

