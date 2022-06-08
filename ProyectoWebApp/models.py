from django.db import models


# Create your models here.

class Compra(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    banco = models.CharField(max_length=40)
    paquete = models.CharField(max_length=40)
    nrotarjeta = models.IntegerField()
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - E-mail: {self.email} - Banco: {self.banco} - Paquete: {self.paquete} - Nº:Tarjeta: {self.nrotarjeta}.'

class Comentario(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    texto = models.CharField(max_length=140)
    def __str__(self) -> str:
        return f'Comentario de: {self.nombre} {self.apellido}; Comentario: {self.texto}'

class Paquete(models.Model):
    nombre = models.CharField(max_length=40)
    destino =models.CharField(max_length=40)
    hotel = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}; Destino: {self.destino}; Hotel: {self.hotel}'
