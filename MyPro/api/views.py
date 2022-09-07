from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
def Student_details (request,pk):
    stu = Student.objects.get (id = pk)
    serializer = StudentSerializer (stu)
    json_data = JSONRenderer ().render (serializer.data)
    return HttpResponse (json_data,content_type = 'application/json')
    # return JsonResponse (json_data, safe = False)


def Student_list (request):
    stu = Student.objects.all ()
    serializer = StudentSerializer (stu,many = True)
    json_data = JSONRenderer ().render (serializer.data)
    return HttpResponse (json_data,content_type = 'application/json')
    # return JsonResponse (json_data, safe = False)


@api_view (['POST',])
def registration_view (request):
    if request.method == 'POST':
        serializer = StudentSerializer (data = request.data)
        data = {}
        if serializer.is_valid ():
            stu = serializer.save ()
            data['name'] = 'successfully registered new user.'
            data['roll'] = stu.roll
            data['city'] = stu.city
        else:
            data = serializer.errors
        return Response(data)
