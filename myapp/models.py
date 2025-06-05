from django.db import models

# Create your models here.
# Dejo este de prueba se puede borrar en cualquier momento

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del producto")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción del producto")
    precio = models.DecimalField(max_digits=5, decimal_places=2, help_text="Precio del producto")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría")

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del cliente")
    email = models.EmailField(unique=True, help_text="Correo electrónico del cliente")
    telefono = models.CharField(max_length=20, blank=True, null=True, help_text="Teléfono del cliente")

    def __str__(self):
        return self.nombre

