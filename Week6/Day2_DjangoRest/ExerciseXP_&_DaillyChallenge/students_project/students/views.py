from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

class Student_list(APIView):
    def get(self,request):
        date_joined_param = request.GET.get('date_joined')
        if date_joined_param:
            students = Student.objects.filter(date_joined=date_joined_param)
        else:
            students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    # def get(self, request, *args, **kwargs):
    #     students = Student.objects.all()
    #     serializer = StudentSerializer(students, many=True)
    #     return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class Student_detail(APIView):
    def get_object(self, pk):
        student_object = get_object_or_404(Student,id=pk)
    
    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'Message': f'Deleted student: {student.first_name}'})
    