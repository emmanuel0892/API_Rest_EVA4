from django.db import models

class Nivel_Academico(models.Model):
    cod_nivelA = models.AutoField(primary_key=True)
    nombre_nivel = models.TextField(max_length=50)

    def __str__(self):
        return str(self.nombre_nivel)

class Asignaturas(models.Model):
    cod_asignatura = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return str(self.nombre)

class Docentes(models.Model):
    rutDocente = models.CharField(max_length=10, primary_key=True)
    nombre = models.TextField(max_length=50)
    apellidoP = models.TextField(max_length=50)
    apellidoM = models.TextField(max_length=50)
    sexo = models.TextField(max_length=50)

    def __str__(self):
        return str(self.rutDocente) + "  " + str(self.nombre) + "  " + str(self.apellidoP) + "  " + str(self.apellidoM)

class Alumnos(models.Model):
    rutAlumno = models.CharField(max_length=10, primary_key=True)
    nombre = models.TextField(max_length=50)
    apellidoP = models.TextField(max_length=50)
    apellidoM = models.TextField(max_length=50)
    sexo = models.TextField(max_length=50)
    nivel_academico = models.ForeignKey(Nivel_Academico, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rutAlumno) + " - " + str(self.nombre) + " - " + str(self.apellidoP) + " - " + str(self.apellidoM) + " - " + str(self.sexo) + " - " + str(self.nivel_academico)

class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nivel_academico = models.ForeignKey(Nivel_Academico, on_delete=models.CASCADE)
    rutDocente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_curso) + " - " + str(self.nivel_academico) + " - " + str(self.rutDocente) + " - " + str(self.asignatura)