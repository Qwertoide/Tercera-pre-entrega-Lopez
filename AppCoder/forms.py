from django import forms

class curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()



class alumno_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    curso = forms.CharField(max_length=20)


class profesor_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    profesion = forms.CharField(max_length=20)
    

class entregable_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()