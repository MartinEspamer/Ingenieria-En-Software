from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Preguntas, Eleccion
from  django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = "encuestas/index.html" #template a utilizar
    context_object_name = "ultimas_preguntas_list" #nombre del contexto a utilizar

    def get_queryset(self): #metodo para obtener las preguntas
        return Preguntas.objects.order_by("-fecha_publicacion") #obtiene todas las preguntas

class DetalleView(generic.DetailView):
    model = Preguntas #modelo a utilizar
    template_name = "encuestas/detalle.html" #template a utilizar

class ResultadosView(generic.DetailView):
    model = Preguntas #modelo a utilizar
    template_name = "encuestas/resultados.html" #template a utilizar


def voto(request, pk):
    pregunta = get_object_or_404(Preguntas, pk=pk)
    try:
        seleccion = pregunta.eleccion_set.get(pk=request.POST["eleccion"])
    except (KeyError, Eleccion.DoesNotExist):
        return render(request, 'encuestas/detalles.html', {
            'preguntas': pregunta,
            'error_message': "No seleccionaste una opcion.",
        })
    else:
        seleccion.votos += 1
        seleccion.save()
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(pregunta.id,)))
