from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante, Carrera
from django.template import loader
from django.http import Http404


# Create your views here.

def index(request):
    return HttpResponse("Hola a todos desde myfirstapp")

def detalles(request, estudiante_id):
    return HttpResponse("Detalles del estudiante %s." % estudiante_id)

def carreras(request, estudiante_id):
    return HttpResponse("Carreras del estudiante %s." % estudiante_id)

def agrega_carrera(request, estudiante_id):
    return HttpResponse("Agregando una carrera a %s." % estudiante_id)

def index(request):
    estudiantes = Estudiante.objects.order_by("nombre")
    context = {
    "estudiantes": estudiantes,
    }
    return render(request, "myfirstapp/index.html", context)

def detalles(request, estudiante_id):
    try:
        estudiante = Estudiante.objects.get(pk=estudiante_id)
    except Estudiante.DoesNotExist:
        raise Http404()
    return render(request, "myfirstapp/detalles.html", 
    {"estudiante": estudiante})
