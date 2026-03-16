from django.shortcuts import render
from .models import Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'proyectos.html', {'proyectos': proyectos})