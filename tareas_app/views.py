from django.shortcuts import render
from .models import Tarea

# Create your views here.

def listar_tareas(request):
    # Obtener las tareas para pasarle despues al render
    tareas = Tarea.objects.all()

    # Pasar como parametro para que pueda mostrar todo
    return render(request, 'listar_tareas.html', {'tareas': tareas})
