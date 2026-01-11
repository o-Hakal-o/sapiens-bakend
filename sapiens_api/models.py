from django.db import models
Genders = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]


class User(AbstractUser):
    
    id = models.BigAutoField(primary_key = True)
    Nombre_de_Usuario  = models.Charfield(max_length = 24)
    Alias = models.Charfield(max_Length = 14)
    Sexo = models.CharField(max_length= 1 , choices = Genders)
    Contrasenna = models.TextField(max_Length = 24 , blank = True )
    Avatar = models.ImageField(upload_to = 'media/avatars' , null = true , blank = true) 

    def __str__(self):
        return self.name
    