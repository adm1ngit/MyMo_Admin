from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from .serializers import LoginSerializer
from rest_framework import views, status
from rest_framework.response import Response

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"detail": "Successfully logged in."}, status=status.HTTP_200_OK)