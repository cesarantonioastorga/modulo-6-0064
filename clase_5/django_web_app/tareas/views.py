from django.shortcuts import get_object_or_404, render, redirect
from .models import Proyecto, Tarea
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm, TareaForm

@login_required
def lista_proyectos(request):

    #proyectos = Proyecto.objects.all()
    proyectos = Proyecto.objects.filter(usuario=request.user) #filtra proyectos de usuario

    return render(request, 'proyectos.html', {
        'proyectos': proyectos
    })

#Formulario crear proyecto

@login_required
def crear_proyecto(request):

    if request.method == "POST":

        form = ProyectoForm(request.POST)

        if form.is_valid():

            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()

            return redirect('proyectos')

    else:
        form = ProyectoForm()

    return render(request, 'crear_proyecto.html', {
        'form': form
    })


#Formulario crear tarea
@login_required
def crear_tarea(request, proyecto_id):

    # 🔐 Asegura que el proyecto pertenece al usuario
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=request.user)

    if request.method == "POST":

        form = TareaForm(request.POST)

        if form.is_valid():

            tarea = form.save(commit=False)
            tarea.proyecto = proyecto  # 👈 asignamos el proyecto
            tarea.save()

            return redirect('proyectos')  # o a detalle del proyecto

    else:
        form = TareaForm()

    return render(request, 'crear_tarea.html', {
        'form': form,
        'proyecto': proyecto
    })

@login_required
def detalle_proyecto(request, proyecto_id):

    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=request.user)
    tareas = proyecto.tarea_set.all()

    if request.method == "POST":
        form = TareaForm(request.POST)

        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()

            return redirect('detalle_proyecto', proyecto_id=proyecto.id)

    else:
        form = TareaForm()

    return render(request, 'detalle_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas,
        'form': form
    })


@login_required
def toggle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    tarea.completada = not tarea.completada
    tarea.save()

    return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)