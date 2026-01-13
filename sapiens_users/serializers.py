from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Nombre_de_Usuario', 'gmail', 'rol', 'Alias', 'Avatar', 'Sexo', 'Nota']
        read_only_fields = ['gmail', 'rol']

class StudentRegisterSerializer(serializers.ModelSerializer):
    # Definimos 'password' como write_only para que no se devuelva en el JSON
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['Nombre_de_Usuario', 'gmail', 'password', 'username']

    def create(self, validated_data):
        # Si no envían username, usamos el gmail
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('gmail')
            
        validated_data['rol'] = User.Role.ESTUDIANTE
        
        # create_user tomará el campo 'password' de validated_data 
        # automáticamente y lo encriptará.
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