from .serializers import ArticuloSerial,Articulo,Tipo_publicacion,Tipo_publicacionSerial,Categoria,CategoriaSerial,ComentarioSerial,Comentario
from rest_framework.viewsets import ModelViewSet

class ArticuloView(ModelViewSet):
    serializer_class = ArticuloSerial
    queryset = Articulo.objects.all()
    
class Tipo_publicacionView(ModelViewSet):
    serializer_class = Tipo_publicacionSerial
    queryset = Tipo_publicacion.objects.all()
    
class CategoriaView(ModelViewSet):
    serializer_class = CategoriaSerial
    queryset = Categoria.objects.all()
    
class ComentarioView(ModelViewSet):
    serializer_class = ComentarioSerial
    queryset = Comentario.objects.all()

