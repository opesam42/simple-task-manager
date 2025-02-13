from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
""" class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='./upload', blank=True, null=True)
    # Pillow library needed for imageField

    def __str__(self):
        return self.user.username """

class CustomUser(AbstractUser):
    bio = models.TextField()
    profileImage = models.ImageField(upload_to='./upload', blank=True, null=True)
    # Pillow library needed for imageField

    def __str__(self):
        return self.username
