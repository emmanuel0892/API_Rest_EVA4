from django.contrib import admin
from Colegio.models import Nivel_Academico,Asignaturas,Docentes,Alumnos,Cursos

class Nivel_Academico_Admin(admin.ModelAdmin):
    list_display=['cod_nivelA','nombre_nivel']

admin.site.register(Nivel_Academico, Nivel_Academico_Admin)

class Asignaturas_Admin(admin.ModelAdmin):
    list_display=['cod_asignatura','nombre']

admin.site.register(Asignaturas,Asignaturas_Admin)

class Docentes_Admin(admin.ModelAdmin):
    list_display=['rutDocente','nombre','apellidoP','apellidoM','sexo']

admin.site.register(Docentes,Docentes_Admin)

class Alumnos_Admin(admin.ModelAdmin):
    list_display=['rutAlumno','nombre','apellidoP','apellidoM','sexo','nivel_academico']

admin.site.register(Alumnos,Alumnos_Admin)

class Cursos_Admin(admin.ModelAdmin):
    list_display=['id_curso','nivel_academico','rutDocente','asignatura']

admin.site.register(Cursos,Cursos_Admin)