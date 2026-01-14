from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    # Al usar ImageField aquí, habilitamos de nuevo la carga de archivos
    Avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['Nombre_de_Usuario', 'Alias', 'rol', 'Avatar', 'gmail', 'Sexo', 'Nota', 'Fecha_nacimiento']
        read_only_fields = ['gmail', 'rol']

    def to_representation(self, instance):
        """Este método controla cómo se ven los datos al salir (GET)"""
        representation = super().to_representation(instance)
        # Si existe el avatar, forzamos que devuelva la URL de Cloudinary
        if instance.Avatar:
            representation['Avatar'] = instance.Avatar.url
        return representation
    
from rest_framework import serializers
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class StudentRegisterSerializer(serializers.ModelSerializer):
    # Definimos el password con un mínimo de 8 caracteres directamente aquí
    password = serializers.CharField(
        write_only=True, 
        min_length=8, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['Nombre_de_Usuario', 'gmail', 'password', 'username']

    def validate_gmail(self, value):
        """
        Valida que el correo tenga un formato estándar y sea único.
        """
        # Expresión regular estándar para correos electrónicos
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, value):
            raise serializers.ValidationError("El formato del correo electrónico no es válido.")
        
        # Verificar si ya existe en la base de datos
        if User.objects.filter(gmail=value.lower()).exists():
            raise serializers.ValidationError("Este correo ya está registrado en la plataforma.")
            
        return value.lower()

    def validate_password(self, value):
        """
        Valida que la contraseña cumpla con: 8+ caracteres, números, mayúsculas y minúsculas.
        """
        # 1. Verificar números
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("La contraseña debe incluir al menos un número.")
            
        # 2. Verificar mayúsculas
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("La contraseña debe incluir al menos una letra mayúscula.")
            
        # 3. Verificar minúsculas
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("La contraseña debe incluir al menos una letra minúscula.")
            
        return value

    def validate_Nombre_de_Usuario(self, value):
        """
        Asegura que el nombre de usuario no sea demasiado corto.
        """
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")
        return value

    def create(self, validated_data):
        # Extraemos la contraseña para manejarla con el método seguro de Django
        raw_password = validated_data.pop('password')
        
        # Si no se envía username, usamos el gmail como nombre de usuario interno
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('gmail')
            
        # Asignamos el rol por defecto
        validated_data['rol'] = User.Role.ESTUDIANTE

        # Creamos el usuario. 
        # NOTA: Asegúrate de que tu modelo User acepte el argumento 'Contraseña' 
        # o cámbialo a 'password' si es el estándar de Django.
        user = User.objects.create_user(
            Contraseña=raw_password, 
            **validated_data
        )
        
        return user

class LoginSerializer(serializers.Serializer):
    gmail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # authenticate usa el USERNAME_FIELD definido en el modelo (gmail)
        user = authenticate(username=data.get('gmail'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")