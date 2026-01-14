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
class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['Nombre_de_Usuario', 'gmail', 'password', 'username']

    def create(self, validated_data):
        # 1. Extraemos el password del diccionario
        raw_password = validated_data.get('password')
        
        # 2. Aseguramos el username
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('gmail')
            
        validated_data['rol'] = User.Role.ESTUDIANTE

        # 3. Creamos el usuario pasando explícitamente 'Contraseña'
        # para evitar el error de nulidad en tu base de datos.
        user = User.objects.create_user(
            Contraseña=raw_password, 
            **validated_data
        )
        
        # IMPORTANTE: Este return debe estar alineado dentro de la función create
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