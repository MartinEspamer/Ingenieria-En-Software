from django.db import models
from django.utils import timezone
import datetime

class Preguntas(models.Model):
	texto_preguntas = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField("fecha publicacion")
	def __str__(self):
		return self.texto_preguntas
	def fue_publicado_recientemente(self):
		return self.fecha_publicacion >= timezone.now()-datetime.timedelta(days=1)

class Eleccion(models.Model):
	pregunta = models.ForeignKey ( Preguntas, on_delete=models.CASCADE )
	texto_elegido = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
	def _str__(self):
		return self.texto_elegido

