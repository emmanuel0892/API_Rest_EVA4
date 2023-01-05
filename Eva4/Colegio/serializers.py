from rest_framework import serializers
from Colegio.models import Nivel_Academico,Asignaturas,Docentes,Alumnos,Cursos

class Nivel_Academico_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel_Academico
        fields = "__all__"

class Asignaturas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Asignaturas
        fields = "__all__"

class Docentes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Docentes
        fields = "__all__"

class Alumnos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = "__all__"

class Cursos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = "__all__"