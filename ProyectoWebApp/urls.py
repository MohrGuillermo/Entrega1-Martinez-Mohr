from django.urls import path

from ProyectoWebApp.views import *
urlpatterns = [
    path('', inicio, name='Inicio'),
    path('Paquetes/', verPaquetes, name='Paquetes'),
    path('Blog/', verComentarios, name='Blog'),
    path('Nosotros/', nosotros, name='Nosotros'),
    path('NuevoComentario/', formComentarios , name='NuevoComentario'),
    path('NuevoPaquete/', formPaquetes , name='NuevoPaquete'),
    path('NuevaCompra/', comprasForm , name='NuevaCompra'),
    path('busquedaCompra/', buscarCompra, name = 'buscarCompra' ),
    path('buscar/',buscar,name = 'Buscar')
    
]
