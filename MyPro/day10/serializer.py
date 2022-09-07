from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # def validate_seat(self,value):
    #     if int(value) > 100:
    #         raise serializers.ValidationError ('Seats are full.')
    #     return value
