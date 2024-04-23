from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    promedio = models.FloatField(default=9.99)
    foraneo = models.BooleanField(default=False)
class Carrera(models.Model):
    LICENCIATURA = 1
    INGENIERIA = 2
    OPCIONES_TIPO = (
    (LICENCIATURA, "Licenciatura"),
    (INGENIERIA, "Ingenieria"),
    )
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=OPCIONES_TIPO, null=True, blank=True)
    nombre = models.CharField(max_length=200)