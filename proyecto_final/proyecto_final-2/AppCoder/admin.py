from django.contrib import admin


# Register your models here.

from .models import Curso,Profesor,Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    pass