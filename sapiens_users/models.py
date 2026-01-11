from django.db import models
from django.contrib.auth.models import AbstractUser
Genders = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]


class User(AbstractUser):
    
    id = models.BigAutoField(primary_key = True)
    Nombre_de_Usuario  = models.CharField(max_length = 24)
    Alias = models.CharField(max_length = 14)
    Avatar = models.ImageField(upload_to = 'media/avatars' , null = True , blank = True) 
    Sexo = models.CharField(max_length= 1 , choices = Genders)
    Nota = models.CharField(max_length = 240)
    Fecha_nacimiento = models.DateField()
    Contrasenna = models.TextField(max_length = 24 , blank = True )
    
    def __str__(self):
        return self.name
    