from django.db import models
import string
import random


def generateRandomCode():
    length = 16
    valid_chars = string.printable
    while True:
        code = ''.join(random.choices(valid_chars, k=length))
        if Task.objects.filter(task_code=code).count() == 0:
            break
    return code

"""
After setting up authentication
class User(models.Model):
    user_code = models.CharField(max_length=16, unique=True, default=generateRandomCode)
"""

# Create your models here.
class Task(models.Model):
    task_code = models.CharField(max_length=16, unique=True, default=generateRandomCode)
    user = models.CharField(max_length=50, unique=True)
    task_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
