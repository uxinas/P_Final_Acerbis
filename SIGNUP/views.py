from django.http import HttpResponse
from django.shortcuts import render
from SIGNUP.models import Usuario_nuevo
from SIGNUP.forms import *


def signup(request):
    return render(request,'signup.html')


def Usuario_nuevo_Formulario_vista(request):
    if request.method == "POST":
        miFormulario = Usuario_nuevo_Formulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Usuario_nuevo (nombre=informacion['nombre'], 
                            email=informacion['email'],
                            password=informacion['password'])
            usuario.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = Usuario_nuevo_Formulario()
        return render(request, 'signup.html', {'miFormulario':miFormulario})



    
