from django.shortcuts import render
from .models import Movie

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .serializer import MovieSerializer


# Create your views here.
def front (request):
    mymovie = Movie.objects.all ().values ()
    template = loader.get_template ('front.html')
    context = {
        'mymovie': mymovie,
    }
    return HttpResponse (template.render (context,request))


def addmov (request):
    template = loader.get_template ("addmov.html")
    return HttpResponse (template.render ({},request))


def addmovrecord (request):
    x = request.POST['title']
    y = request.POST['release_date']
    z = request.POST['seat']
    movie = Movie(title = x,release_date = y,seat = z)
    movie.save ()
    return HttpResponseRedirect (reverse ('front'))
