from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('proyectos/', views.lista_proyectos, name='proyectos'),
    path('accounts/login/', auth_views.LoginView.as_view(
    authentication_form=LoginForm
), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('proyectos/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyectos/<int:proyecto_id>/tarea/nueva/', views.crear_tarea, name='crear_tarea'),
    path('tarea/<int:tarea_id>/toggle/', views.toggle_tarea, name='toggle_tarea'),
]

