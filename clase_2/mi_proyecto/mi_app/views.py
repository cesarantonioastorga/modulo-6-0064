from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django!")

def inicio(request):
    return render(request, "index.html")