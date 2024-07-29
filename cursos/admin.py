from django.contrib import admin
from .models import *

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('cod_asignatura', 'nombre_curso', 'tiene_lab', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_asignatura', 'nombre_curso')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()

admin.site.register(Asignatura, AsignaturaAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('cod_docente', 'nombre', 'apellido_paterno', 'apellido_materno', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_docente', 'nombre', 'apellido_paterno', 'apellido_materno')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()

admin.site.register(Docente, DocenteAdmin)

class AulaLabAdmin(admin.ModelAdmin):
    list_display = ('cod_salon_lab', 'aforo', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_salon_lab',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()

admin.site.register(AulaLab, AulaLabAdmin)

class AulaTeoAdmin(admin.ModelAdmin):
    list_display = ('cod_salon_teo', 'aforo', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_salon_teo',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()

admin.site.register(AulaTeo, AulaTeoAdmin)

class CursoLabAdmin(admin.ModelAdmin):
    list_display = ('cod_curso','cod_asignatura', 'grupo', 'cod_docente', 'cod_salon', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_curso', 'grupo')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()

admin.site.register(CursoLab, CursoLabAdmin)

class CursoTeoAdmin(admin.ModelAdmin):
    list_display = ('cod_curso', 'grupo', 'cod_docente', 'cod_salon', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_curso', 'grupo')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()
        
admin.site.register(CursoTeo, CursoTeoAdmin)
