from django.contrib import admin
from .models import CambioGrupo, Solicitudes, Respuestas

class CambioGrupoAdmin(admin.ModelAdmin):
    list_display = ('cod_asignatura', 'cui_solicitante', 'cui_donante', 'curso_solicitante', 'curso_donante', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_asignatura__cod_asignatura', 'cui_solicitante__cui', 'cui_donante__cui')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()

admin.site.register(CambioGrupo,CambioGrupoAdmin)

class SolicitudesAdmin(admin.ModelAdmin):
    list_display = ('cui_solicitante', 'curso_solicitante','curso_donante', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cui_solicitante__cui', 'curso_solicitante__cod_curso','curso_donante__cod_curso')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()
admin.site.register(Solicitudes,SolicitudesAdmin)

class RespuestasAdmin(admin.ModelAdmin):
    list_display = ('solicitud', 'ofrezco', 'interesado', 'created', 'modified', 'user_id')
    search_fields = ('solicitud__cui_solicitante__cui', 'ofrezco__cod_curso','interesado__cui')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()
admin.site.register(Respuestas,RespuestasAdmin)