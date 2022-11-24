import datetime
from django.db import models


class post(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__ (self):
        return self.title


# class Attendance(models.Model):
#     employee = models.ForeignKey(Employee,on_delete = models.CASCADE, related_name = 'emp_attendance')
#     date = models.DateField(default = datetime.date.today(),null=True)
#     chin = models.TimeField(null = True, blank=True)
#     chout = models.TimeField(null = True, blank=True)
#     remarks = models.CharField(max_length = 255,blank = True)
