from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members




def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index1.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def add(request):
  template = loader.get_template('addmov.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(fname=x, lname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))


