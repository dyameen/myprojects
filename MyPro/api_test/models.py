from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model ()


class Users (models.Model):
    username = models.CharField ("username",max_length = 255)
    password = models.CharField ("password",max_length = 255)

    def __str__ (self):
        return self.username
