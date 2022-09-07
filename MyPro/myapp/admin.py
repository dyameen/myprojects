from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Users)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)