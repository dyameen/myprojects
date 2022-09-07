from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index,name = 'index'),
    path ('new/',views.new,name = "new"),
    # path('pagenotfound/', views.pagenotfound , name="pagenotfound"),
    path ('add/',views.add,name = "add"),
    path ('QuerySet/',views.QuerySet,name = 'QuerySet'),
    path ('QuerySetSC/',views.QuerySetSC,name = 'QuerySetSC'),
    path ('filter/',views.filter,name = 'filter'),
    path ('add/addrecord/',views.addrecord,name = 'addrecord'),
    path ('delete/<int:id>',views.delete,name = 'delete'),
    path ('update/<int:id>',views.update,name = 'update'),
    path ('update/updaterecord/<int:id>',views.updaterecord,name = 'updaterecord'),

]
