<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para cambio de grupo de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2024/07/28</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>31-Jul-2024</td><td>FECHA FIN:</td>
        <td>28-Jul-2024</td>
    </tr>
    <tr>
        <td colspan="3">INTEGRANTES:
        <ul>
        <li>Betanzos Rosas Taylor Anthony - tbetanzos@unsa.edu.pe</li>
        <li>Castillo Lazo Rodrigo Zarun - rcastillola@unsa.edu.pe</li>
        <li>Coaquira Suyo Gabriela Dayana - gcoaquirasu@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]


##  Tipo de Sistema
    Se trata de una aplicación web construida con el framework Django 4, que permita la inscripción y cambios de grupos de los alumnos en los horarios de laboratorios establecidos cada inicio de semestre.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a través de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistema debe permitir gestionar los laboratorios y profesores.
    - RQ04 : El sistema debe permitir solicitar y aceptar un cambio de grupo de laboratorio.

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Laboratorios : En esta entidad se almacena los datos del grupo de laboratorio al que se pueden matricular los alumnos.
    -   Cursos : En esta entidad se almacena los datos del curso de teoria al que se pueden matricular los alumnos.
    -   Cambio de grupo : En esta entidad se almacena los datos del cambio de grupo. Por ejemplo: asignatura, CUI_solicitante, CUI_donante, etc.
    -   Solicitudes : En esta entidad se almacena los datos de las solicitudes de cambio de grupo ingresados por los estudiantes. Por ejemplo: CUI_solicitante, curso_solicitante, curso_donante, etc.
    -   Respuestas : En esta entidad se almacena los datos de las respuestas a las solicitudes de cambio de grupo ingresadas por los estudiantes interesados. Por ejemplo: solicitud, ofrenda, alumno_interesado, etc.
    -   Asignatura : En esta entidad se almacena los datos del curso a los que se puede inscribir el estudiante. Ejemplo: asignatura, curso, tiene_laboratorio, etc.
    -   Docente : En esta entidad se almacena los datos de los profesores que se responsabilizan del avance académico en la enseñanza de los temas planificados en cada curso. Ejemplo: codigo_docente, nombre, apellido, etc.
    -   Aula de laboratorio : En esta entidad se almacena los datos del aula donde se dará la clase de laboratorio. Ejemplo: salon, aforo, estado, etc.
    -   Aula de teoría: En esta entidad se almacena los datos del aula donde se dará la clase teórica de la asignatura. Ejemplo: salon, aforo, estado, etc.
    -   Estudiante : En esta entidad se almacena los datos de los estudiantes matriculados. Ejemplo: CUI, nombre, apellido, etc.


##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| Laboratorios | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| CUI | Numérico | No | Si | Ninguno | Alumno |
| cod_curso  | Numérico | No | No | Ninguno | CursoLab |


| Cursos | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| CUI | Numérico | No | Si | Ninguno | Alumno |
| cod_curso  | Numérico | No | No | Ninguno | CursoTeo |


| CambioGrupo | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cod_asignatura | Numérico | No | Si | Ninguno | Asignatura |
| cui_solicitante  | Numérico | No | No | Ninguno | solicitante |
| cui_donante  | Numérico | No | No | Ninguno | donante |
| curso_solicitante  | Cadena | No | No | Ninguno | curso_solicitante |
| curso_donante  | Cadena | No | No | Ninguno | curso_donante |


| Solicitudes | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cui_solicitante | Numérico | No | Si | Ninguno | solicitante |
| curso_solicitante  | Cadena | No | No | Ninguno | curso_solicitante |
| curso_donante  | Cadena | No | No | Ninguno | curso_donante |


| Respuestas | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Solicitud  | Solicitud  | No | No | Ninguno | solicitud |
| Ofrezco | Cadena | No | Si | Ninguno | curso_ofrecido |
| Interesado  | Alumno | No | No | Ninguno | alumno_interesado |


| Asignatura | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cod_asignatura | Numérico  | No | Si | Ninguno | cod_asignatura |
| nombre_curso | Cadena | No | Si | Ninguno | nombre_curso |
| tiene_lab | Booleano | No | No | Ninguno | tiene_laboratorio |


| Docente | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cod_docente  | Numérico  | No | Si | Ninguno | cod_docente |
| nombre | Cadena | No | Si | Ninguno | nombre |
| apellido_paterno | Cadena | No | No | Ninguno | apellido_paterno |
| apellido_materno | Cadena | No | No | Ninguno | apellido_materno |


| AulaLab | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cod_salon_lab | Cáracter  | No | Si | Ninguno |  cod_salon_lab |
| aforo | Numérico | No | Si | Ninguno | aforo |


| AulaTeo | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cod_salon_teo | Cáracter  | No | Si | Ninguno |  cod_salon_teo |
| aforo | Numérico | No | Si | Ninguno | aforo |


| Alumno | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| cui  | Numérico  | No | Si | Ninguno | cui |
| nombre | Cadena | No | Si | Ninguno | nombre |
| apellido_paterno | Cadena | No | Si | Ninguno | apellido_paterno |
| apellido_materno | Cadena | No | Si | Ninguno | apellido_materno |


##  Diagrama Entidad-Relación

<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Diagrama-Entidad-Relacion-1.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>


## Diagra de procesos
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Diagrama-Entidad-Relacion-2.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

##  Administración con Django
    A continuación se muestra un link que muestra el desarrollo back end [Link](https://lucid.app/lucidspark/2169bab1-ffaf-4f27-8aa1-e185e98646f1/edit?invitationId=inv_b7404b2e-e518-4dc9-a9ba-1e5fefdea924&page=0_0#/ "Desarrollo back end").

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de cambio de matriculas tiene valor de aceptación para los clientes finales (alumnos) radica en realizar el proceso de cambio de grupo de laboratorio propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno puede matricularse en un grupo de laboratorio.
    3. El alumno visualiza la lista de laboratorios donde está inscrito.
    4. El alumno llena un formulario si desea mandar una solicitud para cambio de grupo.
    5. El alumno puede revisar la lista de solicitudes a cambios de grupos y aceptar la solicitud que desee.
    6. El alumno puede ver la información de cada curso de laboratorio y de los docentes a cargo.
    7. El alumno puede ver el consolidado de sus inscripciones.
    8. El alumno cierra sesión.

    A continuación se muestran las actividades realizadas para la construcción de las paginas principales:
    


##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondrá a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
## Funciones
    Página de login en la cual internamente se identifica si el usuario es alumno o docente
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001610.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Inicio como administrador posibilidad de agregar docente y grupos de laboratorio
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/panelinicio.PNG?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Vista de Profesores
    Capacidad de agregar profesores a su vez de editar 
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001728.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001843.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Capacidad de agregar laboratorios y ver laboratorios
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001903.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001946.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20001959.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>



    Acciones como alumno
    Vista al ingresar como alumno
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002034.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Acciones de matricularme a un laboratorio y ver mis laboratorios
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002058.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    capacidad de anular mi matricula a grupo de laboratorio
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002129.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Mandar solicitudes de cambio de laboratorios
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002204.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Lista de solicitudes de laboratorios
<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002325.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>

    Lista de respuestas para aceptar solicitudes

<td style="width:25%;"><img src="https://github.com/TAYTOS/Proyecto-final-pweb2/blob/main/readme/Captura%20de%20pantalla%202024-07-29%20002432.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>





Github del proyecto: https://github.com/TAYTOS/proyecto_final-pweb.git


Arquitectura desarrollo back-end:https://lucid.app/lucidspark/2169bab1-ffaf-4f27-8aa1-e185e98646f1/edit?invitationId=inv_b7404b2e-e518-4dc9-a9ba-1e5fefdea924&page=0_0#

Modelo entidad relacion: https://lucid.app/lucidchart/3526162e-ef47-4f6c-a6e2-4a1ea9dfbaab/edit?invitationId=inv_78891cc9-36db-4b42-9627-b9843970e02b&page=0_0#

Videos: https://drive.google.com/drive/folders/1aHSe-90NDMnjfCZ2UY4ctKMznIvl0msU?usp=sharing




## REFERENCIAS
-   https://fips.unsa.edu.pe/ingenieriadesistemas/plan-de-estudios-2017/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/TAYTOS/Proyecto-final-pweb2.git

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]


