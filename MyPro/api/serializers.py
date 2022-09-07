from rest_framework import serializers
from .models import Student


# normal serialization

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def save (self):
        stu = Student (
            name = self.validated_data['name'],
            roll = self.validated_data['roll'],
            city = self.validated_data['city']
        )
        stu.save()
        return stu

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField (max_length = 100)
#     roll = serializers.IntegerField ()
#     city = serializers.CharField (max_length = 100)
#
#     def create (self,validated_data):
#         return Student.objects.create (**validated_data)
