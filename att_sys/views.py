from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def index (request):
    return HttpResponse ("Attendance system!")
