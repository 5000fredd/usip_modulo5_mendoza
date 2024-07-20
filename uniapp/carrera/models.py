from django.db import models
from .validators import validation_maestro, validar_cedula
from django.core.validators import EmailValidator
from carrera import validators

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre

class Maestro(models.Model):
    nombre = models.CharField(max_length=60, unique=True, validators=[validation_maestro,])
    apellido = models.CharField(max_length=60, unique=True, validators=[validation_maestro,])

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    hora = models.TimeField(blank=True)
    aula = models.CharField(max_length=30, unique=True)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=100)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=12, unique=True, validators=[validar_cedula,])

    def __str__(self):
        return self.nombre


