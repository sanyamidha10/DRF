import imp
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print('stu----->' , stu)
    serializer = StudentSerializer(stu)
    # print('serializer---->',serializer)
    # print('serializer.data --->',serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print('json_data---->',json_data)
    return HttpResponse(json_data, content_type='application/json')


def student_list(request):
    stu = Student.objects.all()
    
    serializer = StudentSerializer(stu, many=True)
    
    # json_data = JSONRenderer().render(serializer.data)
    
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
