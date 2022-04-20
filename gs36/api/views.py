from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']    
    ordering_fields = ['-name']   
    # If we dont give any ordering_fields all will be implemented and you will have options in studentapi list while viewing.   
    