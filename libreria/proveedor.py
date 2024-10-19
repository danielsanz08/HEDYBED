from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.nombre
