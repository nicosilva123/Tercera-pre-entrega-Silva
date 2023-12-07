from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class CursoBuscarFormulario(forms.Form):
    curso = forms.CharField()
    
    
class ProfesorFromulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    profesion = forms.CharField()
    
class ProfesorBuscarFormulario(forms.Form):
    nombre = forms.CharField()
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    
class EstudianteBuscarFormulario(forms.Form):
    nombre = forms.CharField()