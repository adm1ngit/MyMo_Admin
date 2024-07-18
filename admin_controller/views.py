from rest_framework import generics, permissions
from .models import Media
from .serializers import MediaSerializer

class MediaListCreateView(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class MediaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
