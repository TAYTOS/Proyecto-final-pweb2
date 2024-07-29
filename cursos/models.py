from django.db import models
from django.contrib.auth.models import User

status_opciones = [
    ('A', 'Activo'),
    ('I', 'Inactivo')
]

class Asignatura(models.Model):
    cod_asignatura = models.CharField(max_length=8, primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    tiene_lab = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    
    def __str__(self):
        return self.nombre_curso

class Docente(models.Model):
    cod_docente = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_apellido_paterno(self, apellido):
        self.apellido_paterno = apellido
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno
    def set_cod_docente(self, cod_docente):
        self.cod_docente = cod_docente

    def __str__(self):
        return f"{self.nombre} "

class AulaLab(models.Model):
    cod_salon_lab = models.CharField(max_length=8, primary_key=True)
    aforo = models.IntegerField()
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)

    def __str__(self):
        return self.cod_salon_lab

class AulaTeo(models.Model):
    cod_salon_teo = models.CharField(max_length=8, primary_key=True)
    aforo = models.IntegerField()
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)

    def __str__(self):
        return self.cod_salon_teo

class CursoLab(models.Model):
    cod_curso = models.CharField(max_length=9, primary_key=True)
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=50)
    cod_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    cod_salon = models.ForeignKey(AulaLab, on_delete=models.CASCADE)
    aforo = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)

    def __str__(self):
        return self.cod_curso

class CursoTeo(models.Model):
    cod_curso = models.CharField(max_length=8, primary_key=True)
    grupo = models.CharField(max_length=50)
    cod_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    cod_salon = models.ForeignKey(AulaTeo, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_opciones, default='A')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)

    def __str__(self):
        return self.cod_curso
