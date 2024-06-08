from rest_framework import serializers
from .models import Teacher, Student, Class


""" 
This Serializer is responsible for the TeacherViewSet 
"""


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.save()
        return instance


""" 
This Serializer is responsible for the StudentViewSet 
"""


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.save()
        return instance


""" 
This Serializer is responsible for the ClassViewSet 
"""


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

    def create(self, validated_data):
        return Class.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
