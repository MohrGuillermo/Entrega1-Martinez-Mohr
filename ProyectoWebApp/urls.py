from django.urls import path

from ProyectoWebApp.views import comprasForm, inicio, verPaquetes, nosotros, verComentarios, formComentarios, formPaquetes
urlpatterns = [
    path('', inicio, name='Inicio'),
    path('Paquetes/', verPaquetes, name='Paquetes'),
    path('Blog/', verComentarios, name='Blog'),
    path('Nosotros/', nosotros, name='Nosotros'),
    path('NuevoComentario/', formComentarios , name='NuevoComentario'),
    path('NuevoPaquete/', formPaquetes , name='NuevoPaquete'),
    path('NuevaCompra/', comprasForm , name='NuevaCompra'),
    
]
