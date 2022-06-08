from django.urls import path
from ProyectoWebApp.views import inicio, servicios, blog, nosotros, ingreso
urlpatterns = [
    path('', inicio, name='Inicio'),
    path('Servicios/', servicios, name='Servicios'),
    path('Comentarios/', blog, name='Comentarios'),
    path('Nosotros/', nosotros, name='Nosotros'),
    path('Ingreso/', ingreso, name='Ingreso'),
]
