from django.urls import path
from Colegio import views

urlpatterns = [
    path('', views.ListarTodo),
    path('ListarAlumnos/', views.ListarAlumnos),
    path('ListarDocentes/', views.ListarDocentes),
    path('ListarAsignaturas/', views.ListarAsignaturas),
    path('ListarNivelesAcademicos/', views.ListarNivelesAcademicos),
    path('ListarCursos/', views.ListarCursos),
    #alumnos
    path('alumnos/', views.alumnos_list),
    path('alumnos/<str:rut>', views.alumnos_detail),
    #docentes
    path('docentes/', views.docentes_list),
    path('docentes/<str:rut>', views.docentes_detail),
    #asignaturas
    path('asignaturas/', views.asignaturas_list),
    path('asignaturas/<int:id>', views.asignatura_detail),
]
