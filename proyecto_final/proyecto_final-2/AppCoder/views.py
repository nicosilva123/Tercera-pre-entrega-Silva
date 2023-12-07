from datetime import date
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import Curso,Profesor,Estudiante

from .forms import *
from AppCoder.models import *

def Lista_todo(request):
    profesores = Profesor.objects.all()
    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/leer_todo.html", {"profesores":profesores,"cursos":cursos,"estudiantes":estudiantes})

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")
    

def cursos_buscar_view(request):
    if request.method == "GET":
        form = CursoBuscarFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = CursoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for curso in Curso.objects.filter(curso=informacion["curso"]):
                cursos_filtrados.append(curso)

            contexto = {"cursos": cursos_filtrados}         
            return render(request, "AppCoder/leer_todo.html", contexto)

def crea_curso(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(curso=data["curso"],camada = data["camada"])
            curso.save()
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})
    else:
        miFormulario = CursoFormulario()
        return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def eliminar_curso(request, id):
    if request.method == 'POST':
        cursos = Curso.objects.get(id=id)
        cursos.delete()
        
        cursos = Curso.objects.all()
        profesores = Profesor.objects.all()
        estudiantes = Estudiante.objects.all()
        return render(request, "AppCoder/leer_todo.html", {"profesores":profesores,"cursos":cursos,"estudiantes":estudiantes})
    
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            curso.curso=data["curso"]
            curso.camada=data["camada"]
            curso.save()
            
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/leer_todo.html", {"miFormulario":miFormulario})
    else:

        miFormulario = CursoFormulario(initial={
            "curso":curso.curso,
            "camada":curso.camada,
        })
        
        return render(request, "AppCoder/editarCurso.html", {"miFormulario":miFormulario, "id":curso.id})

def crea_profesor(request):
    if request.method == "POST":
        miFormulario = ProfesorFromulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido = data["apellido"], email = data["email"], profesion = data["profesion"])
            profesor.save()
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})
    else:
        miFormulario = ProfesorFromulario()
        return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})
    
def profesor_buscar(request):
    if request.method == "GET":
        form = ProfesorBuscarFormulario()
        return render(
            request,
            "AppCoder/profesor_buscar.html",
            context={"form": form}
        )
    else:
        formulario = ProfesorBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesores_filtrados = []
            for nombre in Profesor.objects.filter(nombre=informacion["nombre"]):
                profesores_filtrados.append(nombre)

            contexto = {"profesores": profesores_filtrados}         
            return render(request, "AppCoder/leer_todo.html", contexto)
        
def eliminar_profesor(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        
        cursos = Curso.objects.all()
        profesores = Profesor.objects.all()
        estudiantes = Estudiante.objects.all()
        return render(request, "AppCoder/leer_todo.html", {"profesores":profesores,"cursos":cursos,"estudiantes":estudiantes})

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        miFormulario = ProfesorFromulario(request.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            profesor.nombre=data["nombre"]
            profesor.apellido=data["apellido"]
            profesor.email=data["email"]
            profesor.profesion=data["profesion"]
            profesor.save()
            
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario})
    else:

        miFormulario = ProfesorFromulario(initial={
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "email":profesor.email,
            "profesion":profesor.profesion
        })
        
        return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "id":profesor.id})
    
def crea_estudiante(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=data["nombre"],apellido = data["apellido"], email = data["email"])
            estudiante.save()
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario})
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario})
    
def estudianteBuscar(request):
    if request.method == "GET":
        form = EstudianteBuscarFormulario()
        return render(
            request,
            "AppCoder/estudianteBuscar.html",
            context={"form": form}
        )
    else:
        formulario = EstudianteBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiantes_filtados = []
            for nombre in Estudiante.objects.filter(nombre=informacion["nombre"]):
                estudiantes_filtados.append(nombre)

            contexto = {"estudiantes": estudiantes_filtados}         
            return render(request, "AppCoder/leer_todo.html", contexto)
        
def eliminar_estudiante(request, id):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(id=id)
        estudiante.delete()
        
        cursos = Curso.objects.all()
        profesores = Profesor.objects.all()
        estudiantes = Estudiante.objects.all()
        return render(request, "AppCoder/leer_todo.html", {"profesores":profesores,"cursos":cursos,"estudiantes":estudiantes})

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            estudiante.nombre=data["nombre"]
            estudiante.apellido=data["apellido"]
            estudiante.email=data["email"]
            estudiante.save()
            
            return redirect("AppCoder:leer_todo")
        return render(request, "AppCoder/editarEstudiante.html", {"miFormulario":miFormulario})
    else:

        miFormulario = EstudianteFormulario(initial={
            "nombre":estudiante.nombre,
            "apellido":estudiante.apellido,
            "email":estudiante.email,
        })
        
        return render(request, "AppCoder/editarEstudiante.html", {"miFormulario":miFormulario, "id":estudiante.id})



# class CursoList(ListView):
#     model = Curso
#     template_name = 'AppCoder/cursos_list.html'
#     context_object_name = "cursos"
    
# class CursoDatail(DeleteView):
#     model = Curso
#     template_name = 'AppCoder/curso_detail.html'
#     context_object_name = "curso"
    
# class CursoCreate(CreateView):
#     model = Curso
#     template_name = 'AppCoder/curso_formulario_avanzado.html'
#     fields = ["curso","camada"]
#     success_url = "/AppCoder/cursos/todos"
    
# class CursoUpdate(UpdateView):
#     model = Curso
#     template_name = 'AppCoder/curso_Update.html'
#     fields = ["curso","camada"]
#     success_url = "/AppCoder/cursos/todos"
    
# class CursoDelete(DeleteView):
#     model = Curso
#     template_name = 'AppCoder/curso_delete.html'
#     success_url = "/AppCoder/cursos/todos"