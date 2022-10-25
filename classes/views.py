from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view (['GET', 'POST'])

def Course_list (request, format = None):
    if request.method == 'GET':
        courses = Course.objects.all ()
        serializer = CourseSerializer (courses, many=True)
        return JsonResponse ({"courses": serializer.data})

    if request.method == 'POST':
        serializer = CourseSerializer (data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)

@api_view (['GET','PUT', 'DELETE'])

def Course_detail (request, id, format = None):
        try:
            courses = Course.objects.get (pk=id)
        except Course.DoesNotExit:
            return Response (status=status.HTTP_404_NOT_FOUND) 

        if request.method == 'GET':
            serializer = CourseSerializer (courses)
            return Response (serializer.data) 

        elif request.method == 'PUT':
            serializer = CourseSerializer (courses, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response (serializer.data)  
            return Response (serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
            courses.delete()
            return Response (status=status.HTTP_204_NO_CONTENT)


       


           



