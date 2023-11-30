from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
"""
def index(request): #luego del def el nombre de la vista
    #para chequear si viene por get o post:
    if request.method == "GET":
        return HttpResponse("Hola mundo parte 2")
    elif request.method == "POST":
        return HttpResponse('')       
"""
def index(request):
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha' : datetime.now()
    }
    return render(request, "index.html", context)

def alumnos_listado(request):
    listado = [
            'Carlos Lopez',
            'Maria del Cerro',
            'Juan Perez'
        ]
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': True,
        'cant_inscriptos': len(listado),
        'listado_alumnos': listado
    }
    
    return render(request, 'alumnos_listado.html', context)

def alumno_detalle(request, nombre_alumno):
    return HttpResponse(
    f"""
    <h1>Bienvendid@ {nombre_alumno}</h1>
    <p>Página personal de usuario</p>
    """
    )
    
def alumnos_historico(request, year):
    return HttpResponse(f'Historico de alumnos del año: {year}')

def alumnos_estado(request, estado):
    return HttpResponse(f'El estado del alumno se encuentra {estado}')