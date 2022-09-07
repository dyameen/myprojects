from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class test_view (APIView):
    def get (self,request,*args,**kwargs):
        data = {
            'name': 'yameen',
            'age': 29,
        }
        return Response (data)

    def post (self,request,*args,**kwargs):
        serializer = post_serializer (data = request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else:
            return Response (serializer.errors)

#Create your views here.
def test_view(request):
    data = {
        'name' : 'yameen',
        'age'  : 29,
    }
    return JsonResponse(data)
