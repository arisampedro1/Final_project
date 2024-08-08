from django.contrib import admin
from .models import Experiencia, Aprendiz, Mentor, Actividad, NivelDeAprendizaje

# Register your models here.


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'camada')

@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'experiencia', 'nivel')
    list_filter = ('nivel', 'experiencia')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'experiencia')
    list_filter = ('experiencia',)
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_de_entrega', 'nivel', 'experiencia', 'aprendiz')
    list_filter = ('fecha_de_entrega', 'nivel', 'experiencia')
    search_fields = ('nombre',)

@admin.register(NivelDeAprendizaje)
class NivelDeAprendizajeAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)