from django.db import models
from django.contrib.auth.models import User

status_opciones = [
    ('A', 'Activo'),
    ('I', 'Inactivo')
]
class Alumno(models.Model):
    cui = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
