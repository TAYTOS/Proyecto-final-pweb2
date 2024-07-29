from django.shortcuts import render
from .models import AsignacionLab
# Create your views here.
from cursos.views import autentifiToken, autentifiGroupAlumno
from django.contrib.auth.models import User
from estudiantes.models import Alumno
from cursos.models import CursoLab,AulaLab
from django.shortcuts import get_object_or_404,render, redirect, HttpResponseRedirect

def mislaboratorios(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        alumno = Alumno.objects.get(user_id = request.COOKIES.get('id')).cui
        mislabs = AsignacionLab.objects.filter( cui = alumno)
        return render(request, 'mislaboratorios.html', {'mislabs': mislabs})
    else:
        return redirect('/login') 

def matricularme(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        if request.method == 'GET':
            laboratorios = CursoLab.objects.all()
            return render(request, 'matricularme.html', {'laboratorios': laboratorios})
         
    else:
        return redirect('/login')
def coincidencias(request,cod_curso):
    miscursos = AsignacionLab.objects.filter(cui = Alumno.objects.get(user_id = request.COOKIES.get('id')).cui)
    for i in miscursos:
        a = str(i.cod_curso)
        b = str(cod_curso)
        if a[-7:] == b[-7:]:
            return True
    return False

def validarMatricula(request, cod_curso):
    if autentifiToken(request) and autentifiGroupAlumno(request):
            alumno = Alumno.objects.get(user_id = request.COOKIES.get('id'))
            lab = CursoLab.objects.get(cod_curso = cod_curso)
            user = User.objects.get(pk=request.COOKIES.get('id'))
            aula = AulaLab.objects.get(cod_salon_lab = lab.cod_salon)
            if not coincidencias(request,cod_curso)  and aula.aforo > lab.aforo:     
                AsignacionLab.objects.create(cui = alumno, cod_curso = lab, user_id = user)
                lab.aforo = lab.aforo + 1
                lab.save()
                return redirect('/mislaboratorios')
            else:
                 return redirect('/matricula')  
    else:
        return redirect('/login')

def desmatricularme(request, cod_curso):
    if autentifiToken(request) and autentifiGroupAlumno(request):
            cod_curso = cod_curso
            AsignacionLab.objects.filter(cui = Alumno.objects.get(user_id = request.COOKIES.get('id')).cui, cod_curso = cod_curso).delete()
            lab = CursoLab.objects.get(cod_curso = cod_curso)
            lab.aforo = lab.aforo - 1
            lab.save()
            return redirect('/mislaboratorios')
    else:
        return redirect('/login')