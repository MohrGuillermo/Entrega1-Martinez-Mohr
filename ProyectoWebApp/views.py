from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):

    return render(request, 'ProyectoWebApp/inicio.html')


def servicios(request):

    return render(request, 'ProyectoWebApp/servicios.html')


def blog(request):

    return render(request, 'ProyectoWebApp/blog.html')


def nosotros(request):

    return render(request, 'ProyectoWebApp/nosotros.html')


def ingreso(request):

    return render(request, 'ProyectoWebApp/ingreso.html')