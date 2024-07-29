from django.db import models
from django.contrib.auth.models import User
from estudiantes.models import Alumno
from cursos.models import CursoLab, CursoTeo


status_opciones = [
    ('A', 'Activo'),
    ('I', 'Inactivo')
]
class AsignacionLab(models.Model):
    cui = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cod_curso = models.ForeignKey(CursoLab, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    class Meta:
        unique_together = ('cui', 'cod_curso')

    def __str__(self):
        return f"{self.cui} - {self.cod_curso}"

class AsignacionTeo(models.Model):
    cui = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cod_curso = models.ForeignKey(CursoTeo, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    class Meta:
        unique_together = ('cui', 'cod_curso')

    def __str__(self):
        return f"{self.cui} - {self.cod_curso}"
