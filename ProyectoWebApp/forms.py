from django import forms

# ACA VAMOS A DETERMINAR CADA UNO DE LOS FORMULARIOS MEDIANTE LOS CUALES INGRESAREMOS LOS DISTINTOS OBJETOS A LA PAGINA. (SIGUE EN VIEWS.PY)

class ComentarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=140)

class CompraForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    banco = forms.CharField(max_length=40)
    paquete = forms.CharField(max_length=40)
    nrotarjeta = forms.IntegerField()


    nrotarjeta = forms.IntegerField()

class PaqueteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    destino = forms.CharField(max_length=40)
    hotel = forms.CharField(max_length=40)

