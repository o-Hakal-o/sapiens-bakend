from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken # <--- IMPORTANTE
from .models import User
from .serializers import StudentRegisterSerializer, LoginSerializer, UserProfileSerializer

# VISTA DE PERFIL (CRUD)
class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
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
        user = serializer.validated_data # El validate del serializer ya devuelve al user
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'token_acceso': str(refresh.access_token),
            'token_refresh': str(refresh),
            'user': UserProfileSerializer(user).data
        }, status=status.HTTP_200_OK)