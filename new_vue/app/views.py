from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


class PostView(generics.RetrieveAPIView):
    queryset = post.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many = True)
        return Response(serializer.data)
