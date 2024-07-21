from rest_framework import generics, request, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView

class VideoListCreateAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDeleteAPIView(generics.DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
