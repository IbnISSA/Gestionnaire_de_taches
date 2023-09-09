from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Created_at = models.DateField(auto_now_add=True)
    Finished_at = models.DateField(null=True, blank=True)
    Completed = models.BooleanField(default=False)