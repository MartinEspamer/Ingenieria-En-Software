from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Preguntas, Eleccion
from  django.shortcuts import render, get_object_or_404
from django.urls import reverse
def index(request,pregunta_id):
    pregunta = get_object_or_404(Preguntas, pk=pregunta_id) #obtiene la pregunta por su id
    return render(request, 'encuestas/index.html', {"pregunta":pregunta}) #renderiza la plantilla index.html

def detalle(request, pregunta_id):
    return HttpResponse("estas viendo la pregunta %s." %pregunta_id)

def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Preguntas, pk=pregunta_id) #obtiene la pregunta por su id
    return render(request, 'encuestas/resultados.html', {"pregunta":pregunta}) #renderiza la plantilla resultados.html
    
def voto(request, pregunta_id):
    pregunta = get_object_or_404(Preguntas, pk=pregunta_id) #obtiene la pregunta por su id
    try:
        seleccion = pregunta.eleccion_set.get(pk=request.POST["eleccion"]) #obtiene la eleccion por su id
    except (KeyError, Eleccion.DoesNotExist):
        return render(request, 'encuestas/index.html', {
            'pregunta':pregunta,
            'error_message':"No seleccionaste una opcion.",
        })
    else:
        seleccion.votos += 1 #incrementa el voto
        seleccion.save() #guarda el voto en la base de datos
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(pregunta.id,))) #redirecciona a la vista resultados

