from django import forms
from django.contrib.auth.models import User
from .models import Docente, CursoLab

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password' ]
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['cod_docente', 'nombre','apellido_paterno','apellido_materno'] 
        
class CursoLabForm(forms.ModelForm):
    class Meta:
        model = CursoLab
        fields = ['grupo','cod_docente','cod_salon']