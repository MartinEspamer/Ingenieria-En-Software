from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas, Eleccion
from django.template import loader
def index(request):
    ultima_pregunta_list = Preguntas.objects.order_by('-pub_date')[:5]
    salida = ', '.join([p.question for p in ultima_pregunta_list])
    template = loader.get_template('encuestas/index.html')
    contexto = {'ultima_pregunta_list': ultima_pregunta_list}
    #une las preguntas con una coma y un espacio
    return HttpResponse(template.render(contexto, request))

def detalle(request, pregunta_id):
    return HttpResponse("estas viendo la pregunta %s." %pregunta_id)

def resultados(request, pregunta_id):
    response = "estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def voto(request, pregunta_id):
    return HttpResponse("estas votando la pregunta %s." % pregunta_id)

