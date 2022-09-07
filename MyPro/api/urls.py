from django.urls import path
from . import views

urlpatterns = [
    path ('stuinfo/<int:pk>',views.Student_details),
    path ('stuinfo/',views.Student_list),
    path ('register/',views.registration_view),
]
