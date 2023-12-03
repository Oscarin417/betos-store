from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    correo = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    mensaje = models.TextField(null=False)
    condiciones = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre