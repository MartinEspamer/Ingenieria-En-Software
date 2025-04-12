from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, Estamos en el index de encuestas")

def detalle(request, pregunta_id):
    return HttpResponse("estas viendo la pregunta %s." %pregunta_id)

def resultados(request, pregunta_id):
    response = "estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def voto(request, pregunta_id):
    return HttpResponse("estas votando la pregunta %s." % pregunta_id)

