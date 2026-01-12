from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from .serializers import StudentRegisterSerializer, LoginSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.response import Response


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated] # Solo usuarios logueados

    def get_object(self):
        # Esto garantiza que el CRUD sea sobre el usuario que hace la petición
        return self.request.user
    
    
# VISTA DE REGISTRO
class StudentRegisterView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = [AllowAny]

# VISTA DE LOGIN
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'token_acceso': str(refresh.access_token),
            'token_refresh': str(refresh),
            'user': UserProfileSerializer(user).data
        })
class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Esto hace que el CRUD sea sobre el usuario logueado
        return self.request.user