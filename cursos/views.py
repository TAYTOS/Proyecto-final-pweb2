from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, DocenteSerializer,CursoLabSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404,render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from cursos.models import Docente,Asignatura,CursoLab
from rest_framework.decorators import authentication_classes, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication  
from django.contrib.auth.models import Group
from .forms import UserForm, DocenteForm,CursoLabForm
from django.urls import reverse
#t$PaTd9c
def autentifiToken(request):
    id = request.COOKIES.get('id')
    token = request.COOKIES.get('Token')
    print(token)
    if(Token.objects.filter(user_id=id, key=token).exists()):
        return True
    else:
        return False
def autentifiGroupDocente(request):
    id = request.COOKIES.get('id')
    user = User.objects.get(pk=id)
    usuarios_en_grupo_admin = Group.objects.get(name='admin').user_set.all()
    if user in usuarios_en_grupo_admin:
        return True
    else:
        return False
def autentifiGroupAlumno(request):
    id = request.COOKIES.get('id')
    user = User.objects.get(pk=id)
    usuarios_en_grupo_alumno = Group.objects.get(name='alumno').user_set.all()
    if user in usuarios_en_grupo_alumno:
        return True
    else:
        return False
@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return inicio(request)
    print(request.data)
    usuario = get_object_or_404(User, username=request.data['username'])
    if not usuario.check_password(request.data['password']):
        return redirect('/login')
    token, created = Token.objects.get_or_create(user=usuario)
    #seccion para verificar si el usuario pertenece a un determinado grupo
    usuarios_en_grupo_admin = Group.objects.get(name='admin').user_set.all()
    usuarios_en_grupo_alumno = Group.objects.get(name='alumno').user_set.all()
    if usuario in usuarios_en_grupo_admin:
        response = HttpResponseRedirect('/administrador/')
        response.set_cookie('Token', token.key)
        response.set_cookie('id', usuario.id)
        return response #error al mandar el dos cookies 
    elif usuario in usuarios_en_grupo_alumno:
        response = HttpResponseRedirect('/alumno/')
        response.set_cookie('Token', token.key)
        response.set_cookie('id', usuario.id)
        return response #error al mandar el dos cookies 
    else:
        return Response({'error': 'invalid user'}, status=status.HTTP_400_BAD_REQUEST)
def logout(request):
    response = HttpResponseRedirect('/login')
    Token.objects.filter(key=request.COOKIES.get('Token')).delete()
    response.delete_cookie('Token')
    response.delete_cookie('id')
    return response #se redirige a la vista de login

def inicio(request):
    form = UserForm(request.GET or None)
    serializer = DocenteSerializer()
    if form.is_valid():
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'inicio.html', context)

def docentes(request):
    if autentifiToken(request) and autentifiGroupDocente(request):
        docentes = Docente.objects.all().values()
        return render(request, 'docentes.html', {'docentes': docentes})
    else:
        return redirect('/login') 
def asignaturas(request):
    if autentifiToken(request) and autentifiGroupDocente(request):
        asignaturas = Asignatura.objects.all().values()
        return render(request, 'asignaturas.html', {'asignaturas': asignaturas})
    else:
        return redirect('/login')
def laboratorios(request):
    if autentifiToken(request) and autentifiGroupDocente(request):
        laboratorios = CursoLab.objects.all()
        docentes = Docente.objects.all().values()
        return render(request, 'laboratorios.html', {'laboratorios': laboratorios})
    else:
        return redirect('/login')
@api_view(['POST','GET'])
def registrarDocentes(request):
    if autentifiToken(request) and autentifiGroupDocente(request):
        form = DocenteForm(request.GET or None)
        user = User.objects.get(pk=request.COOKIES.get('id'))
        if request.method == 'POST':
            serializer = DocenteSerializer(data={'cod_docente':request.data.get('cod_docente'),'nombre':request.data.get('nombre'),'apellido_paterno':request.data.get('apellido_paterno'),'apellido_materno':request.data.get('apellido_materno'),'user_id':request.COOKIES.get('id')})
            if serializer.is_valid() :
                serializer.save()
                return redirect('/docentes')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            return render(request, 'registrarDocentes.html', {'form': form})
    else:
        return redirect('/login') 
@api_view(['POST','GET'])
def agregarGrupoLab(request, cod_asignatura):
    if autentifiToken(request) and autentifiGroupDocente(request):
        if request.method == 'GET':
            form = CursoLabForm(request.GET or None)
            return render(request, 'registrarGrupoLab.html', {'form': form})
        else :
            grupo= request.data.get('grupo')
            serializer = CursoLabSerializer(data={'cod_asignatura':cod_asignatura,'grupo':request.data.get('grupo'),'cod_docente':request.data.get('cod_docente'),'cod_salon':request.data.get('cod_salon'),'user_id':request.COOKIES.get('id'),'cod_curso':grupo+cod_asignatura})
            if serializer.is_valid():
                serializer.save()
                return redirect('/laboratorios')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #return JsonResponse(serializer.data)
    else:
        return redirect('/login')

def editarDocentes(request, docentes_cod):
    if autentifiToken(request) and autentifiGroupDocente(request):
        if request.method == 'GET':
            docente = get_object_or_404(Docente, cod_docente=docentes_cod)
            form = DocenteForm(request.POST or None, instance=docente)
            return render(request, 'editarDocentes.html', {'docente':docente, 'form': form}   )
        else:
            docente = get_object_or_404(Docente, cod_docente=docentes_cod)
            form = DocenteForm(request.POST or None, instance=docente)
            if form.is_valid():
                form.save()
                return redirect('/docentes')
            return render(request, 'editarDocentes.html', {'docente':docente, 'form': form}   )
    else:
        return redirect('/login') 
def estadoDocente(request, docentes_cod):
    if autentifiToken(request) and autentifiGroupDocente(request):
        docente = get_object_or_404(Docente, cod_docente=docentes_cod)
        if request.method == 'POST':
            if docente.status == "A":
                docente.status = "I"
                docente.save()
            else:
                docente.status = "A"
                docente.save()
        return redirect('/docentes')
    else:
        return redirect('/login') 

@api_view(['GET','POST'])
def administrador(request):
    if autentifiToken(request) and autentifiGroupDocente(request):
        return render(request,'administracion.html')
     #se retorna un mensaje de que se ha logeado correctamente
    else:
        return redirect('/login')
@api_view(['GET','POST'])
def alumno(request):
    if autentifiToken(request) and autentifiGroupAlumno(request):
        return render(request,'alumno.html')
     #se retorna un mensaje de que se ha logeado correctamente
    else:
        return redirect('/login')