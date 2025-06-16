from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    desc = models.TextField(max_length=200, null=False)
    completada = models.BooleanField(default=False)
    modificada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
