from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from .models import *
from myapp.serializer import AuthorSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def new (request):
    if request.method == "GET":
        author = Author.objects.all ()
        serializer = AuthorSerializer (author,many = True)
        return JsonResponse (serializer.data,safe = False)

    elif request.method == "POST":
        jp = JSONParser()
        data = jp.parse (request)
        serializer = AuthorSerializer (data = data)
        if serializer.is_valid ():
            serializer.save ()
            return JsonResponse (serializer.data,status = 201)
        return JsonResponse (serializer.errors,status = 400)


def index (request):
    myuser = Users.objects.all ().values ()
    template = loader.get_template ('index.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse (template.render (context,request))


def add (request):
    template = loader.get_template ("add.html")
    return HttpResponse (template.render ({},request))


def delete (request,id):
    user = Users.objects.get (id = id)
    user.delete ()
    return HttpResponseRedirect (reverse ('index'))


def addrecord (request):
    x = request.POST['username']
    y = request.POST['password']
    user = Users (username = x,password = y)
    user.save ()
    return HttpResponseRedirect (reverse ('index'))


def update (request,id):
    user = Users.objects.get (id = id)
    template = loader.get_template ("update.html")
    context = {
        "user": user,
    }
    return HttpResponse (template.render (context,request))


def updaterecord (request,id):
    user = Users.objects.get (id = id)
    username = request.POST.get ('username')
    password = request.POST.get ('password')
    user.username = username
    user.password = password
    user.save ()
    return HttpResponseRedirect (reverse ('index'))


def QuerySet (request):
    myuser = Users.objects.all ().values ()
    template = loader.get_template ('QuerySet.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse (template.render (context,request))


def QuerySetSC (request):
    myuser = Users.objects.values_list ('username')
    template = loader.get_template ('QuerySetSC.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse (template.render (context,request))


def filter (request):
    # myuser = Users.objects.filter(Q(username='yameen') |Q(id=2)).values()
    # myuser = Users.objects.filter(username = 'yameen', id = 2).values ()
    # myuser = Users.objects.filter(username__startswith='y').values()
    myuser = Users.objects.all ().order_by ('username','-id').values ()
    template = loader.get_template ('filter.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse (template.render (context,request))
