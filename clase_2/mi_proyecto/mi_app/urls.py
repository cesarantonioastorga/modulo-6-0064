from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo, name="saludar"),
    path("",views.inicio, name="inicio")
]