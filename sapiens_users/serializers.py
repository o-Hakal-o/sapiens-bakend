from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Nombre_de_Usuario', 'gmail', 'rol' ,]
        read_only_fields = ['gmail', 'rol'] # No permitimos cambiar correo ni rol por seguridad
class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['Nombre_de_Usuario', 'gmail', 'password']

    def create(self, validated_data):
        # Usamos el gmail como username de Django
        validated_data['username'] = validated_data.get('gmail')
        validated_data['rol'] = User.Role.ESTUDIANTE
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    gmail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data.get('gmail'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Nombre_de_Usuario', 'gmail', 'rol']
        read_only_fields = ['gmail', 'rol']