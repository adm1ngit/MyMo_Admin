from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Students
from .serializers import StudentsSerializer

# Create your views here.

class StudentsView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)