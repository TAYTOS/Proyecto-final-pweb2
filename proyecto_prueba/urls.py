"""
URL configuration for proyecto_prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path, include
from .views import *
from cursos.views import login, administrador, inicio, registrarDocentes, docentes,editarDocentes,logout,autentifiToken, estadoDocente, asignaturas,agregarGrupoLab, alumno,laboratorios
from asignaciones.views import mislaboratorios
from asignaciones.views import matricularme, desmatricularme, validarMatricula
from cambio_matriculas.views import solicitud_cambio_matricula,listar_solicitudes,respuesta,listar_respuestas,validarCambio
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', login),
    re_path('administrador/', administrador),
    path('logout/', logout),
    path('inicio', inicio),
    path('solicitud_cambio_matricula', solicitud_cambio_matricula, name='solicitud_cambio_matricula'),
    path('listar_solicitudes', listar_solicitudes, name='listar_solicitudes'),
    path('listar_respuestas', listar_respuestas),
    path('listar_respuestas/<str:id>', validarCambio, name='validarCambio'),
    path('listar_solicitudes/<str:id>', respuesta,name='respuesta'),
    path('matricula', matricularme),
    path('matricula/<str:cod_curso>/validarmatricula', validarMatricula, name='validarMatricula'),
    path('matricula/', mislaboratorios),
    path('registrarDocentes', registrarDocentes),
    path('docentes', docentes),
    path('mislaboratorios', mislaboratorios),
    path('mislaboratorios/<str:cod_curso>/desmatricularme', desmatricularme, name='desmatricularme'),
    path('verlaboratorios',laboratorios),
    path('laboratorios', asignaturas),
    path('laboratorios/<str:cod_asignatura>/',agregarGrupoLab,name='agregar_grupo'),
    path('docentes/<str:docentes_cod>/',editarDocentes,name='editar_Docentes'),
    path('docentes/<str:docentes_cod>/status/',estadoDocente,name='status_Docentes'),
    path('agregar-docentes', registrarDocentes, name='agregar_docentes'),
    path('alumno/', alumno),
]
