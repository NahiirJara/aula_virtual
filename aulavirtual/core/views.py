from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #luego del def el nombre de la vista
    return HttpResponse("Hola mundo parte 2")  