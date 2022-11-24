from django.db import models
class Members(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

# Create your models her

