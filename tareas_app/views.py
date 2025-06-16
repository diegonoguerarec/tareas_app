from django.shortcuts import render, redirect
from .models import Tarea

# Create your views here.

def listar_tareas(request):
    # Obtener las tareas para pasarle despues al render
    tareas = Tarea.objects.all()

    # Pasar como parametro para que pueda mostrar todo
    return render(request, 'listar_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    # Si se presiona enviar en el formulario, hace esto
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        desc = request.POST.get('desc')

        if request.POST.get('completada') == 'on':
            completada = True
        else:
            completada = False

        Tarea.objects.create(
            nombre = nombre,
            desc = desc,
            completada = completada
        )

        return redirect('agregar_tarea')

    # Sino, solo carga la pagina
    return render(request, 'agregar_tarea.html')
