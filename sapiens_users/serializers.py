from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Nombre_de_Usuario', 'gmail', 'rol', 'Alias', 'Avatar', 'Sexo', 'Nota']
        read_only_fields = ['gmail', 'rol']

class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['gmail', 'password', 'username']

    def create(self, validated_data):
        # Usamos el gmail como el identificador de username interno de Django
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('gmail')
            
        validated_data['rol'] = User.Role.ESTUDIANTE
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    gmail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Importante: authenticate usa el USERNAME_FIELD definido en el modelo
        user = authenticate(username=data.get('gmail'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")