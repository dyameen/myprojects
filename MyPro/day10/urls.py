from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path ('',views.front,name = 'front'),
    path ('addmov/',views.addmov,name = 'addmov'),
    path ('addmov/addmovrecord/',views.addmovrecord,name = 'addmovrecord'),

]
