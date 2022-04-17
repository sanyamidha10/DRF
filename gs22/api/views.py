from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # If we have multiple classes and want to apply same authentication and permission on them , then we can also write some code inside settings.py(globally) rather than writing explicitly in each class like this below one.

    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]



    # Moreover, if you want to override in any class, then you can also do the same by writing the above commented code.