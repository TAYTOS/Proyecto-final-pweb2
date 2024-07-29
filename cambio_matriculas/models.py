from django.db import models
from django.contrib.auth.models import User
from estudiantes.models import Alumno
from cursos.models import Asignatura, CursoTeo, CursoLab

class CambioGrupo(models.Model):
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    cui_solicitante = models.ForeignKey(Alumno, related_name='solicitante', on_delete=models.CASCADE)
    cui_donante = models.ForeignKey(Alumno, related_name='donante', on_delete=models.CASCADE)
    curso_solicitante = models.ForeignKey(CursoLab, related_name='curso_solicitante', on_delete=models.CASCADE)
    curso_donante = models.ForeignKey(CursoLab, related_name='curso_donante', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)


    def __str__(self):
        return f"{self.cod_asignatura} - {self.cui_solicitante} - {self.cui_donante}"
    
class Solicitudes(models.Model):
    cui_solicitante = models.ForeignKey(Alumno, related_name='solicitante_solicitudes', on_delete=models.CASCADE)
    curso_solicitante = models.ForeignKey(CursoLab, related_name='curso_solicitante_solicitudes', on_delete=models.CASCADE)
    curso_donante = models.ForeignKey(CursoLab, related_name='curso_donante_solicitudes', on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)


    def __str__(self):
        return f"{self.cui_solicitante} - {self.curso_solicitante}"
class Respuestas(models.Model):
    solicitud = models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
    ofrezco = models.ForeignKey(CursoLab, related_name='ofrezco', on_delete=models.CASCADE)
    interesado = models.ForeignKey(Alumno, related_name='interesado', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return f"{self.solicitud} - {self.ofrezco} - {self.interesado}"