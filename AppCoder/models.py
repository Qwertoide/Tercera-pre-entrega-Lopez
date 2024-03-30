from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Alumno(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)


class Profesor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=30)


class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
