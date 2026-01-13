from django.db import models

class Articulo(models.Model):
    id_usuario = models.CharField(default=1,blank=True,null=True)
    titulo = models.CharField(max_length=300)
    tipo_publicacion = models.ForeignKey("Tipo_publicacion",on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE)
    contenido = models.CharField(blank=True,null=True)
    portada = models.ImageField(blank=True,null=True,upload_to='media/portadas')
    archivo_adjunto = models.FileField(blank=True,null=True)
    
    def __str__(self):
        return self.titulo
    
class Tipo_publicacion(models.Model):
    nombre = models.CharField(max_length=250) 
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    id_usuario = models.CharField()
    contenido = models.CharField()
    imagen = models.ImageField(blank=True,null=True,upload_to='media/comentarios')
    articulo = models.ForeignKey("Articulo",on_delete=models.CASCADE)
    


