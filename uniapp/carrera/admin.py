from django.contrib import admin
from .models import Clase, Maestro, Seccion, Estudiante 

class ClaseAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class MaestroAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido',)

class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clase', 'hora', 'aula', 'maestro',)
    list_filter = ('nombre', 'clase',)
    search_fields = ('nombre',)
    ordering = ('aula',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'seccion', 'cedula',)
    list_filter = ('nombre', 'apellido',)
    search_fields = ('cedula',)
    ordering = ('nombre',)

admin.site.register(Clase, ClaseAdmin)
admin.site.register(Maestro, MaestroAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Estudiante, EstudianteAdmin)