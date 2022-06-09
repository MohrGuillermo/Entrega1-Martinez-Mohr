


from django.shortcuts import render
from django.http import HttpResponse
from ProyectoWebApp.models import Comentario, Paquete, Compra
from ProyectoWebApp.forms import ComentarioForm, CompraForm, PaqueteForm
 
# Create your views here.
def inicio(request):

    return render(request, 'ProyectoWebApp/inicio.html')


def verPaquetes(request):
    paquetes = Paquete.objects.all()
    contexto = {'paquetes':paquetes}    
    return render(request, 'verPaquetes.html', contexto)
    

def formPaquetes(request):
    if request.method == 'POST':
        miFormulario = PaqueteForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            paquetes = Paquete(nombre = informacion['nombre'], destino = informacion['destino'], hotel = informacion['hotel'])
            paquetes.save()
            return render(request, 'ProyectoWebApp/formCompras.html')
    else:
        miFormulario = PaqueteForm()
    return render(request, 'formPaquetes.html', {'miFormulario' : miFormulario})




def nosotros(request):

    return render(request, 'ProyectoWebApp/nosotros.html')


def comprasForm(request):
    if request.method == 'POST':
        miFormulario = CompraForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            compras = Compra(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], banco = informacion['banco'], paquete = informacion['paquete'], nrotarjeta = informacion['nrotarjeta'])
            compras.save()
            return render(request, 'ProyectoWebApp/gracias.html')
    else:
        miFormulario = CompraForm()
    return render(request, 'formCompras.html', {'miFormulario' : miFormulario})




def verComentarios(request):
    comentarios = Comentario.objects.all()
    contexto = {'comentarios':comentarios}    
    return render(request, 'blog.html', contexto)


def formComentarios(request):

    if request.method == 'POST':
        miFormulario = ComentarioForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            comentario = Comentario(nombre = informacion['nombre'], apellido = informacion['apellido'], texto = informacion['texto'])
            comentario.save()
            return render(request, 'ProyectoWebApp/inicio.html')
    else:
        miFormulario = ComentarioForm()
    return render(request, 'formComentarios.html', {'miFormulario' : miFormulario})


def buscarCompra(request):
    return render(request, 'busquedaCompras.html')

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        compras = Compra.objects.filter(nombre = nombre)

        return render(request, 'resultadosBusqueda.html', {'compras': compras , "nombre":nombre })
    else:
        respuesta = 'No enviaste datos'
        return  HttpResponse(respuesta)

