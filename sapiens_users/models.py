from django.db import models
from django.contrib.auth.models import AbstractUser

Genders = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
]

class User(AbstractUser):
    class Role(models.TextChoices):
        ESTUDIANTE = 'STUDENT', 'Estudiante'
        PROFESOR = 'PROFESSOR', 'Profesor'
        MODERATOR = 'MODERATOR', 'Moderador'
    
    rol = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ESTUDIANTE,
    )
    
    # El id ya lo crea Django por defecto, pero dejarlo como BigAutoField está bien.
    id = models.BigAutoField(primary_key=True)
    Nombre_de_Usuario = models.CharField(max_length=24)
    Alias = models.CharField(max_length=14, blank=True, null=True)
    # Corregido: ruta relativa
    Avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    Sexo = models.CharField(max_length=1, choices=Genders, null=True, blank=True)
    Nota = models.CharField(max_length=240, null=True, blank=True)
    Fecha_nacimiento = models.DateField(null=True, blank=True)
    
    gmail = models.EmailField(unique=True) # Usado para login

    USERNAME_FIELD = 'gmail'  
    REQUIRED_FIELDS = ['username', 'Nombre_de_Usuario'] 

    def __str__(self):
        return f"{self.Nombre_de_Usuario} - {self.rol}"