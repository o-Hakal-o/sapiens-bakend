from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class StudentRegister(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'Nombre_de_Usuario', # 1. Lo que el usuario ve como su nombre
            'gmail',             # 2. Su correo
            'password',          # 3. Su clave
        ]

    def create(self, validated_data):
        # 1. Extraemos la clave
        raw_password = validated_data.pop('password')
        
        # 2. TRUCO: Copiamos el gmail al campo username de Django
        # Así cumplimos con Django sin pedirle un dato extra al usuario
        validated_data['username'] = validated_data.get('gmail')
        
        # 3. Forzamos el rol
        validated_data['rol'] = User.Role.ESTUDIANTE
        
        # 4. Creamos y encriptamos
        user = User(**validated_data)
        user.set_password(raw_password)
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    gmail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('gmail')
        password = data.get('password')

        if email and password:
            # IMPORTANTE: Aquí se usa username=email porque USERNAME_FIELD es 'gmail'
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Correo o contraseña incorrectos.")
        else:
            raise serializers.ValidationError("Debe proveer correo y contraseña.")

        data['user'] = user
        return data