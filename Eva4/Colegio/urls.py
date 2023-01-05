from django.urls import path
from Colegio import views

urlpatterns = [
    path('ListarAlumnos/', views.ListarAlumnos),
    path('ListarDocentes/', views.ListarDocentes),
    path('ListarAsignaturas/', views.ListarAsignaturas),
    path('ListarNivelesAcademicos/', views.ListarNivelesAcademicos),
    path('ListarCursos/', views.ListarCursos),
]
