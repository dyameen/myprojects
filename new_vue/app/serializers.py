from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import *


# User Serializer

# Register Serializer
class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

