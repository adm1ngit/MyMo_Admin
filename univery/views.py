from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Institute, FacultyRoute
from .serializers import *   

class InstituteFacultyRouteApi(APIView):
    def get(self, request):
        institutes = Institute.objects.all()
        serializer = InstituteSerializer(institutes, many=True, context={'request': request})
        response_data = {
            'institutes': serializer.data
        }
        return Response(response_data)

    def post(self, request):
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyRouteListApi(APIView):
    def get(self, request):
        faculties = FacultyRoute.objects.all()
        serializer = FacultyRouteSerializer(faculties, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultyRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
