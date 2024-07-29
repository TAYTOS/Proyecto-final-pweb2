from django.shortcuts import render, redirect
from django.http import JsonResponse
from cursos.models import CursoLab,AulaLab
from cursos.views import autentifiToken, autentifiGroupAlumno
from estudiantes.models import Alumno
from asignaciones.models import AsignacionLab
from .models import Solicitudes,Respuestas,CambioGrupo
from django.contrib.auth.models import User
import json
def solicitud_cambio_matricula(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        if request.method == 'GET':
            alumno = Alumno.objects.get(user_id = request.COOKIES.get('id')).cui
            mislabs = AsignacionLab.objects.filter( cui = alumno)
            grupos = CursoLab.objects.all()
            return render(request, 'mandarsolicitud.html', {'mislabs': mislabs, 'grupos': grupos})
        else:
            data = json.loads(request.body)
            cod_grupo_donante = data.get('cod_grupo_donante')
            cod_grupo_solicitante = data.get('cod_grupo_solicitante')
            grupo_donante = CursoLab.objects.get(cod_curso = cod_grupo_donante)
            grupo_solicitante = CursoLab.objects.get(cod_curso = cod_grupo_solicitante)
            user = Alumno.objects.get(user_id = request.COOKIES.get('id'))
            Solicitudes.objects.create(cui_solicitante = user, curso_solicitante = grupo_solicitante, curso_donante = grupo_donante, user_id = User.objects.get(pk=request.COOKIES.get('id')))
            return render(request, 'mandarsolicitud.html', {'mensaje': 'solicitud enviada'})#modificar redireccion
    else:
        return redirect('/login')
def listar_solicitudes(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        user = Alumno.objects.get(user_id = request.COOKIES.get('id'))
        solicitudes = Solicitudes.objects.exclude(cui_solicitante = user)
        return render(request, 'lista_solicitudes.html', {'solicitudes': solicitudes})
    else:
        return redirect('/login')

def respuesta(request,id) :
    if autentifiToken(request) and autentifiGroupAlumno(request):
        if request.method == 'POST':
            solicitud = Solicitudes.objects.get(pk = id)
            interesado = Alumno.objects.get(user_id = request.COOKIES.get('id'))
            if(AsignacionLab.objects.filter(cui = interesado, cod_curso = solicitud.curso_donante.cod_curso).exists() and not Respuestas.objects.filter(solicitud = solicitud, interesado = interesado).exists()):
                ofrezco = CursoLab.objects.get(cod_curso = solicitud.curso_donante.cod_curso)
                Respuestas.objects.create(solicitud = solicitud, ofrezco = ofrezco, interesado = interesado, user_id = User.objects.get(pk=request.COOKIES.get('id')))
                return redirect('listar_solicitudes')
            else:
                return redirect('listar_solicitudes')
        else:
            return render(request, 'respuesta.html')
    else:
        return redirect('/login')
def listar_respuestas(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        user = Alumno.objects.get(user_id = request.COOKIES.get('id'))
        respuestas = Respuestas.objects.filter(solicitud__cui_solicitante = user)
        return render(request, 'lista_respuestas.html', {'respuestas': respuestas})
    else:
        return redirect('/login')

def validarCambio(request,id):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        if request.method == 'POST':
            respuesta = Respuestas.objects.get(pk = id)
            usersolicitante = User.objects.get(pk=request.COOKIES.get('id'))#usuario solicitante
            alumnosolicitante = Alumno.objects.get(user_id = usersolicitante)#alumno solicitante
            cursosolicitante = CursoLab.objects.get(cod_curso = respuesta.solicitud.curso_solicitante)#curso solicitante 
            asignacionLabsolicitante = AsignacionLab.objects.get(cui = alumnosolicitante, cod_curso = cursosolicitante)
            userDonante = User.objects.get(pk=respuesta.interesado.user_id.id)#usuario donante
            alumnoDonante = Alumno.objects.get(user_id = userDonante)#se extrae alumno del donante usando respuesta
            cursoDonante = CursoLab.objects.get(cod_curso = respuesta.ofrezco)#curso del donanteBnumero
            asignacionLabDonante = AsignacionLab.objects.get(cui = alumnoDonante, cod_curso = cursoDonante)
            asignacionLabDonante.delete()
            asignacionLabsolicitante.delete()
            AsignacionLab.objects.create(cui = alumnosolicitante, cod_curso = cursoDonante, user_id = usersolicitante)
            AsignacionLab.objects.create(cui = alumnoDonante, cod_curso = cursosolicitante, user_id = userDonante)
            CambioGrupo.objects.create(cod_asignatura = cursosolicitante.cod_asignatura, cui_solicitante = alumnosolicitante, cui_donante = alumnoDonante, curso_solicitante = cursosolicitante, curso_donante = cursoDonante, user_id = usersolicitante)
            solicitud_cambio_matricula = Solicitudes.objects.get(pk = respuesta.solicitud.pk)
            solicitud_cambio_matricula.delete()
            respuesta.delete()
            return redirect('/mislaboratorios')
        else:
            return redirect('/mislaboratorios')
    else:
        return redirect('/login')