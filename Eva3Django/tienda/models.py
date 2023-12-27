from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.TextField(max_length=100)
    disponibilidad = models.CharField(max_length=250, verbose_name='Disponibilidad')

    def __str__(self):
         fila = self.nombre
         return fila