from django.contrib import admin

# Register your models here.
from .models import Preguntas, Eleccion

admin.site.register(Preguntas)
admin.site.register(Eleccion)