from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

def user_directory_path(instance, filename):
    # leave it for django, it will handle it
    # filename = f'/profile.jpg'
    return f'user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField()
    profileImage = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    # Pillow library needed for imageField

    def __str__(self):
        return self.username
