from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False) 

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title} by {self.author}"