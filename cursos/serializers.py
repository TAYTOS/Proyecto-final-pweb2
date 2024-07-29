from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Docente,CursoLab
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['cod_docente', 'nombre','apellido_paterno','apellido_materno','user_id']
        
        
class CursoLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoLab
        fields = ['cod_curso','cod_asignatura','grupo','cod_docente','cod_salon', 'user_id']

    

