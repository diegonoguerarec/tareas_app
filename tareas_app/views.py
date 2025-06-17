from django.shortcuts import render, redirect
from .models import Tarea
from django.utils import timezone

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
            completada = completada,
            modificada = timezone.now()
        )

        return redirect('agregar_tarea')

    # Sino, solo carga la pagina
    return render(request, 'agregar_tarea.html')

def editar_tarea(request, id):
    # Obtener la tarea con id a editar
    tarea = Tarea.objects.get(id=id)

    # Si se presiona el boton de actualizar desde agregar_tarea.html
    if request.method == 'POST':
        tarea.nombre = request.POST.get('nombre')
        tarea.desc = request.POST.get('desc')
        
        if request.POST.get('completada') == 'on':
            tarea.completada = True
        else:
            tarea.completada = False

        tarea.modificada = timezone.now()

        tarea.save()

        return redirect('listar_tareas')

    # Enviar la tarea el formulario (el mismo formulario de agregar tarea)
    return render(request, 'agregar_tarea.html', {'tarea': tarea})

