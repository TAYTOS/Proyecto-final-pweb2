from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('cui', 'nombre', 'apellido_paterno', 'apellido_materno', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cui', 'nombre', 'apellido')
    list_filter = ('status', 'created', 'modified')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()

admin.site.register(Alumno, AlumnoAdmin)