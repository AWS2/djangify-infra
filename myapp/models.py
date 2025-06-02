from django.db import models

# Create your models here.
# Dejo este de prueba se puede borrar en cualquier momento

class Prueba(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
