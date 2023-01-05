from django.shortcuts import render
from django.http import JsonResponse
from Colegio.models import Alumnos

def ListarAlumnos(request):
    alumnos = Alumnos.objects.all()
    datos = { "alumnos" : list(alumnos.values('rutAlumno','nombre','apellidoP','apellidoM','sexo','nivel_academico')) }
    return JsonResponse(datos)

def ListarDocentes(request):
    pass

def ListarAsignaturas(request):
    pass

def ListarNivelesAcademicos(request):
    pass

def ListarCursos(request):
    pass