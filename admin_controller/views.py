from rest_framework.response import Response
from .models import VideoApp
from .serializers import VideoAppSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions


class VideoAppView(APIView):

    def get(self, request, format=None):
        candidates = VideoApp.objects.all()
        serializer = VideoAppSerializer(candidates, many=True)
        if serializer:
            response_data = {"videos": serializer.data}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"error": "Not Found 🤷‍♂️"}, status=status.HTTP_404_NOT_FOUND)