from django.db import models

class Preguntas(models.Model):
	texto_preguntas = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField("fecha publicacion")

class Eleccion(models.Model):
	pregunta = models.ForeignKey ( Preguntas, on_delete=models.CASCADE )
	texto_elegido = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
