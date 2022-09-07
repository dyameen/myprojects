from django.contrib import admin
from django.urls import include, path
from . import views
from .views import ContactView, ContactSuccessView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
]
