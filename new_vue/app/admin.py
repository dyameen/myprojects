from django.contrib import admin
from .models import *


@admin.register (post)
class PostAdmin (admin.ModelAdmin):
    list_display = ('id','title','content')


# @admin.register (Employee)
# class EmployeeAdmin (admin.ModelAdmin):
#     list_display = ('id','user','designation','autochout')
#
#
# @admin.register (Attendance)
# class AttAdmin (admin.ModelAdmin):
#     list_display = ('id','employee','date','chin','chout')
