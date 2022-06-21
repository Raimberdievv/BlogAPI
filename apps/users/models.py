from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    tel = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = "profile_image/")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"