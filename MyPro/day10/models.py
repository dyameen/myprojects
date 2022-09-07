from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField (null = False, max_length = 128)
    year = models.IntegerField ()


    def __str__ (self):
        return self.title
