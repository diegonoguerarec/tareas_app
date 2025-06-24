from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar/", views.listar_tareas, name="listar_tareas"),
    path("agregar/", views.agregar_tarea, name="agregar_tarea"),
    path("editar/<int:id>", views.editar_tarea, name="editar_tarea"),
    path("eliminar/<int:id>", views.eliminar_tarea, name="eliminar_tarea"),
]