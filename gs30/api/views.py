from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwMzYyODM4LCJpYXQiOjE2NTAzNjI1MzgsImp0aSI6ImY3NmZmN2MzN2JmNjRkNDZhYzdkNjE5ZjdiZWYzMTJlIiwidXNlcl9pZCI6Mn0.368xRZ_oyGR2s9K-f5E-F2zhKVBI35YY_GcHY9wC8qg'