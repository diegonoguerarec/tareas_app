from django.urls import path

from . import views

urlpatterns = [
    path("listar/", views.listar_tareas, name="listar_tareas"),
    path("agregar/", views.agregar_tarea, name="agregar_tarea"),
    path("editar/<int:id>", views.editar_tarea, name="editar_tarea"),
]