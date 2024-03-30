from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Alumno, Entregable
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import curso_formulario, alumno_formulario, profesor_formulario, entregable_formulario



def inicio(request):
    return render( request , "home.html")


def alumnos(request):
    return render(request, "alumnos.html")


def profesores(request):
    return render(request, "profesores.html")






def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def Curso_formulario(request):

    if request.method == "POST":

        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")





def buscar_curso(request):
    return render(request, "buscar_curso.html")


def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    





def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def Alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = alumno_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos["nombre"] , apellido=datos["apellido"], curso=datos["curso"])
            alumno.save()
            return render(request , "formulario_alumno.html")


    return render (request , "formulario_alumno.html")


def buscar_alumno(request):
    return render(request, "buscar_alumno.html")



def  buscarAlumno(request):

        if request.GET["apellido"]:

            apellido = request.GET["apellido"]
            alumnos = Alumno.objects.filter(apellido__icontains= apellido)
            return render(request , "resultado_busqueda_alumno.html" , {"alumnos":alumnos})
            
        else:
        
            print("Alumno no encontrado")








def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores" : profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def Profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=datos["nombre"] , apellido=datos["apellido"], profesion=datos["profesion"])
            profesor.save()
            return render(request , "formulario_profesor.html")


    return render (request , "formulario_profesor.html")


def buscar_profesor(request):
    return render(request, "buscar_profesor.html")



def  buscarProfesor(request):

        if request.GET["apellido"]:
            apellido = request.GET["apellido"]
            profesores = Profesor.objects.filter(apellido__icontains= apellido)
            return render(request , "resultado_busqueda_profesor.html" , {"profesores":profesores})
        else:
            print("Profesor no encontrado")
            







def ver_entregables(request):
    entregables = Entregable.objects.all()
    dicc = {"entregables" : entregables}
    plantilla = loader.get_template("entregables.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = entregable_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            entregable = Entregable(nombre=datos["nombre"] , fecha_de_entrega=datos["Fecha de entrega"])
            entregable.save()
            return render(request , "formulario_entregable.html")


    return render (request , "formulario_entregable.html")


def buscar_entregable(request):
    return render(request, "buscar_entregable.html")



def  buscarEntregable(request):

        if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            entregables = Entregable.objects.filter(nombre__icontains= nombre)
            return render(request , "resultado_busqueda_entregable.html" , {"entregables":entregables})
        else:
            print("Entregable no encontrado")
            


