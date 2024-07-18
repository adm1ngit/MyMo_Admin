from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from rest_framework.permissions import IsAuthenticated

class UserSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSettingsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return UserSettings.objects.get(user=self.request.user)

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class UserInstituesListCreateAPIView(generics.ListCreateAPIView):
    queryset = userInstitues.objects.all()
    serializer_class = UserInstituesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['institute']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

