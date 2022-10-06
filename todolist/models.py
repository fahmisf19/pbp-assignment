from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    finish = models.CharField(max_length=225, default='not finished')