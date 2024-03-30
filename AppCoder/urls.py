from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name = "home"),

    path("ver_cursos/", views.ver_cursos, name="cursos"),
    path("alta_curso", views.Curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso , name="buscar_curso"),
    path("buscar", views.buscar),

    path("alumnos", views.ver_alumnos , name="alumnos"),
    path("alta_alumno", views.Alumno_formulario, name="alta_alumno"),
    path("buscar_alumno", views.buscar_alumno , name="buscar_alumno"),
    path("buscarAlumno", views.buscarAlumno),

    path("profesores", views.ver_profesores , name="profesores"),
    path("alta_profesor", views.Profesor_formulario, name="alta_profesor"),
    path("buscar_profesor", views.buscar_profesor , name="buscar_profesor"),
    path("buscarProfesor", views.buscarProfesor),

    path("entregables", views.ver_entregables , name="entregables"),
    path("alta_entregable", views.entregable_formulario, name="alta_entregable"),
    path("buscar_entregable", views.buscar_entregable , name="buscar_entregable"),
    path("buscarEntregable", views.buscarEntregable),
    ]