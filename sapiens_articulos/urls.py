from rest_framework import routers
from django.urls import path, include
from .views import ArticuloView,CategoriaView,Tipo_publicacionView,ComentarioView
routers = routers.DefaultRouter()

routers.register("categorias", CategoriaView, 'categorias')
routers.register("tipo_publicacion", Tipo_publicacionView, 'tipo_publicacion')
routers.register("articulo", ArticuloView, 'articulo')
routers.register("comentario", ComentarioView, 'comentario')



urlpatterns = [
    path('',include(routers.urls)),
]