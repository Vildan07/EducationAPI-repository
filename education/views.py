from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Teacher, Student, Class
from .serializers import TeacherSerializer, StudentSerializer, ClassSerializer


# Create your views here.


""" 
This View is responsible for the Teacher model 
"""


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


""" 
This View is responsible for the Student model 
"""


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


""" 
This View is responsible for the Class model 
"""


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
