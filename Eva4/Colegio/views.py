from django.shortcuts import render
from django.http import JsonResponse
from Colegio.models import Alumnos,Docentes,Asignaturas,Nivel_Academico,Cursos

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Colegio.serializers import Nivel_Academico_Serializer,Asignaturas_Serializer,Docentes_Serializer,Alumnos_Serializer,Cursos_Serializer


# LISTAR TODOS LOS REGISTROS
#***********************************************************************************************************************

def ListarTodo(request):
    alumnos = Alumnos.objects.all()
    docentes = Docentes.objects.all()
    asignaturas = Asignaturas.objects.all()
    niveles_academicos = Nivel_Academico.objects.all()
    cursos = Cursos.objects.all()
    datos = { "alumnos" : list(alumnos.values('rutAlumno','nombre','apellidoP','apellidoM','sexo','nivel_academico')),
              "docentes" : list(docentes.values('rutDocente','nombre','apellidoP','apellidoM','sexo')),
              "asignaturas" : list(asignaturas.values('cod_asignatura','nombre')),
              "niveles_academicos" : list(niveles_academicos.values('cod_nivelA','nombre_nivel')),
              "cursos" : list(cursos.values('id_curso','nivel_academico','rutDocente','asignatura')) }
    return JsonResponse(datos)

# ALUMNOS
#***********************************************************************************************************************

def ListarAlumnos(request):
    alumnos = Alumnos.objects.all()
    datos = { "alumnos" : list(alumnos.values('rutAlumno','nombre','apellidoP','apellidoM','sexo','nivel_academico')) }
    return JsonResponse(datos)

# GET o POST
@api_view(['GET','POST'])
def alumnos_list(request):
    if request.method == 'GET':
        alumnos = Alumnos.objects.all()
        ser = Alumnos_Serializer(alumnos, many=True)
        return Response(ser.data)

    #Agregar Registros Nuevos
    if request.method == 'POST':
        ser = Alumnos_Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def alumnos_detail(request, rut):
    try:
        alumnos = Alumnos.objects.get(rutAlumno = rut)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        ser = Alumnos_Serializer(alumnos)
        return Response(ser.data)
    
    if request.method == 'PUT':
        ser = Alumnos_Serializer(alumnos, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        alumnos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# DOCENTES
#***********************************************************************************************************************

def ListarDocentes(request):
    docentes = Docentes.objects.all()
    datos = { "docentes" : list(docentes.values('rutDocente','nombre','apellidoP','apellidoM','sexo')) }
    return JsonResponse(datos)

# GET o PUT Docentes
@api_view(['GET','POST'])
def docentes_list(request):
    if request.method == 'GET':
        docentes = Docentes.objects.all()
        ser = Docentes_Serializer(docentes, many=True)
        return Response(ser.data)

    #Agregar Registros Nuevos de docentes
    if request.method == 'POST':
        ser = Docentes_Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def docentes_detail(request, rut):
    try:
        docentes = Docentes.objects.get(rutDocente = rut)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        ser = Docentes_Serializer(docentes)
        return Response(ser.data)

    if request.method == 'PUT':
        ser = Docentes_Serializer(docentes, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        docentes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ASIGNATURAS
#***********************************************************************************************************************

def ListarAsignaturas(request):
    asignaturas = Asignaturas.objects.all()
    datos = { "asignaturas" : list(asignaturas.values('cod_asignatura','nombre')) }
    return JsonResponse(datos)

@api_view(['GET','POST'])
def asignaturas_list(request):
    if request.method == 'GET':
        asignaturas = Asignaturas.objects.all()
        ser = Asignaturas_Serializer(asignaturas, many=True)
        return Response(ser.data)

    # Agregar nueva asignatura
    if request.method == 'POST':
        ser = Asignaturas_Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def asignatura_detail(request, id):
    try:
        asignaturas = Asignaturas.objects.get(cod_asignatura = id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        ser = Asignaturas_Serializer(asignaturas)
        return Response(ser.data)

    if request.method == 'PUT':
        ser = Asignaturas_Serializer(asignaturas, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        asignaturas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# NIVELES ACADEMICOS
#***********************************************************************************************************************

def ListarNivelesAcademicos(request):
    niveles_academicos = Nivel_Academico.objects.all()
    datos = { "niveles_academicos" : list(niveles_academicos.values('cod_nivelA','nombre_nivel')) }
    return JsonResponse(datos)




# CURSOS
#***********************************************************************************************************************

def ListarCursos(request):
    cursos = Cursos.objects.all()
    datos = { "cursos" : list(cursos.values('id_curso','nivel_academico','rutDocente','asignatura')) }
    return JsonResponse(datos)

#***********************************************************************************************************************