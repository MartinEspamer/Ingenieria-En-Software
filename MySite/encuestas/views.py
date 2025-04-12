from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas, Eleccion
from  django.shortcuts import render
from django.http import Http404
def index(request,pregunta_id):
    try:
        pregunta = Preguntas.objects.get(id=pregunta_id) #obtiene la pregunta por su id
    except Preguntas.DoesNotExist:
        raise Http404("No hay preguntas disponibles.")
    return render(request, 'encuestas/index.html', {"pregunta":pregunta}) #renderiza la plantilla index.html

def detalle(request, pregunta_id):
    return HttpResponse("estas viendo la pregunta %s." %pregunta_id)

def resultados(request, pregunta_id):
    response = "estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def voto(request, pregunta_id):
    return HttpResponse("estas votando la pregunta %s." % pregunta_id)

