"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, DocenteSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404,render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from cursos.models import Docente
from rest_framework.decorators import authentication_classes, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication  
from django.contrib.auth.models import Group
from .forms import UserForm, DocenteForm
from django.urls import reverse

@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return inicio(request)
    print(request.data)
    usuario = get_object_or_404(User, username=request.data['username'])
    if not usuario.check_password(request.data['password']):
        return Response({'error': 'invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=usuario)
    serializer = UserSerializer(instance=usuario)
    #seccion para verificar si el usuario pertenece a un determinado grupo
    usuarios_en_grupo = Group.objects.get(name='admin').user_set.all()
    if usuario in usuarios_en_grupo:
        return HttpResponseRedirect('/administrador',headers= {"Authorization": 'Token '+token.key}) #se redirige a la vista de administrador
    else:
        print("El usuario no es miembro del grupo")
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


def inicio(request):
    form = UserForm(request.POST or None)
    serializer = DocenteSerializer()
    if form.is_valid():
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'inicio.html', context)

#no se utilizara en este proyecto
def docentes(request):
    docentes = list(Docente.objects.all().values())
    return JsonResponse(docentes, safe=False)

@api_view(['POST','GET'])
def registrarDocentes(request):
    serializer = DocenteSerializer(data=request.data)
    user = get_object_or_404(User, id=request.data['user_id'])
    if serializer.is_valid() and user is not None:
        serializer.save()
        return Response({'docente': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
#@authentication_classes([TokenAuthentication]) posteriormente se usara deribados para las otras secciones
def profile(request):
    return Response({'status': 'Profile successful!'})

@api_view(['GET'])
@authentication_classes([TokenAuthentication]) #se define el metodo que utilizara para autentificarse
def administrador(request):
    print(request.user)
    return render(request,'administracion.html') #se retorna un mensaje de que se ha logeado correctamente
    """