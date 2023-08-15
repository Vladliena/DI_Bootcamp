from django.shortcuts import render
from .models import Department, Employee, Task, Project
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    TaskSerializer,
    ProjectSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAuthenticatedAdmin

# Create your views here.


class DepartmentAPIView(APIView):
    
    permission_classes = (IsAuthenticatedAdmin, )
    
    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # def put(self, request, pk: int, *args, **kwargs):  # full update
    #     department = Department.objects.get(id=pk)
    #     serializer = DepartmentSerializer(instance=department, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

    def patch(self, request, pk: int, *args, **kwargs):  # partial update
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(
            instance=department, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk: int, *args, **kwargs):
        department = Department.objects.get(id=pk)
        department.delete()
        return Response({"Message": f"Deleted student: {department.name}"})


class EmployeeAPIView(APIView):
    
    permission_classes = (IsAuthenticatedAdmin, )
    
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk: int, *args, **kwargs):  # partial update
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(
            instance=department, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk: int, *args, **kwargs):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({"Message": f"Deleted student: {employee.name}"})


class TaskAPIView(APIView):
    
    permission_classes = (IsAuthenticatedAdmin, )
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk: int, *args, **kwargs):  # partial update
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(
            instance=department, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk: int, *args, **kwargs):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({"Message": f"Deleted student: {task.name}"})


class ProjectAPIView(APIView):
    
    permission_classes = (IsAuthenticatedAdmin, )
    
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk: int, *args, **kwargs):  # partial update
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(
            instance=department, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk: int, *args, **kwargs):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({"Message": f"Deleted student: {project.name}"})
