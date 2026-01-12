from django.db import models
from django.contrib.auth.models import AbstractUser
Genders = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ]


class User(AbstractUser):
    
    class Role(models.TextChoices):
        ESTUDIANTE = 'STUDENT' , 'Estudiante'
        PROFESOR = 'PROFESSOR' , 'Profesor'
        MODERATOR = 'MODERATOR' , 'Moderador'
    
    rol = models.CharField(
        max_length= 20,
        choices = Role.choices,
        default = Role.ESTUDIANTE,
    )
    id = models.BigAutoField(primary_key = True)
    Nombre_de_Usuario  = models.CharField(max_length = 24)
    Alias = models.CharField(max_length = 14 , blank= True , null = True)
    Avatar = models.ImageField(upload_to = 'media/avatars' , null = True , blank = True) 
    Sexo = models.CharField(max_length= 1 , choices = Genders)
    Nota = models.CharField(max_length = 240)
    Fecha_nacimiento = models.DateField()
    gmail = models.EmailField()
    Contrasenna = models.TextField(max_length = 24 , blank = True )
    
    def __str__(self):
        return f"{self.Nombre_de_Usuario} - {self.rol}"
    