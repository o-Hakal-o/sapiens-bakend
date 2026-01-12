from rest_framework import serializers
from .models import Articulo,Tipo_publicacion,Categoria,Comentario

class Tipo_publicacionSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_publicacion
        fields = '__all__'
        
        
class CategoriaSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class ArticuloSerial(serializers.ModelSerializer):
    tipo_publicacion = Tipo_publicacionSerial(read_only=True)
    tipo_publicacion_id = serializers.PrimaryKeyRelatedField(queryset=Tipo_publicacion.objects.all(),write_only=True,source='tipo_publicacion')
    categoria = CategoriaSerial(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(),write_only=True,source='categoria')
    
    
    
    class Meta:
        model = Articulo
        fields = '__all__'

class ComentarioSerial(serializers.ModelSerializer):
    articulo = ArticuloSerial(read_only=True)
    articulo_id = serializers.PrimaryKeyRelatedField(queryset=Articulo.objects.all(),write_only=True,source='articulo')
    
    
    class Meta:
        model = Comentario
        fields = '__all__'
        
