from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Institute, FacultyRoute, ModelLogo
from .serializers import *

class LogoView(APIView):
    def get(self, request):
        Logo = ModelLogo.objects.all()
        serializer = ModelLogoSerializer(Logo, many=True, context={'request': request})
        return Response(serializer.data)

class InstituteFacultyRouteApi(APIView):

    def get(self, request):
        # Filterlash
        query_params = request.query_params
        institutes = Institute.objects.all()

        # Masalan, nomiga qarab filterlash
        name = query_params.get('name', None)
        if name:
            institutes = institutes.filter(name__icontains=name)

        serializer = InstituteSerializer(institutes, many=True, context={'request': request})
        response_data = {
            'institutes': serializer.data
        }
        return Response(response_data)

    def post(self, request, *args, **kwargs):
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        institute = get_object_or_404(Institute, pk=pk)
        serializer = InstituteSerializer(institute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        institute = get_object_or_404(Institute, pk=pk)
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
