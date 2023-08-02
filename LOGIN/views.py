#from LOGIN.models import Login
from django.http import HttpResponse
from LOGIN.forms import LoginFormulario
from django.shortcuts import render
from LOGIN.models import Login
from SIGNUP.models import Usuario_nuevo
from SIGNUP.views import Usuario_nuevo_Formulario_vista
from SIGNUP.forms import Usuario_nuevo_Formulario



def login(request):
    return render(request,'login.html')


def panelCrud(request):
    return render(request,'leer_usuarios.html')


def loginFormulario_vista(request):
    return render(request,'loginFormulario.html')


def loginFormulario(request):
    if request.method == "POST":
        miFormulario = LoginFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Login(nombre=informacion['nombre'], 
                            email=informacion['email'],
                            password=informacion['password'])
            usuario.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = LoginFormulario()
        return render(request, 'loginFormulario.html', {'miFormulario':miFormulario})


def leerUsuarios(request):
    usuarios = Usuario_nuevo.objects.all()
    contexto = {'Usuarios':usuarios}
    return render(request, 'leer_usuarios.html', contexto)

 

def eliminarUsuarios(request, usuario_nombre):
    usuario = Usuario_nuevo.objects.get(nombre=usuario_nombre)
    usuario.delete()

    usuarios = Usuario_nuevo.objects.all()
    contexto = {'Usuarios':usuarios}

    return render(request, 'leer_usuarios.html', contexto )


def editarUsuarios(request, usuario_nombre):
    usuario = Usuario_nuevo.objects.get(nombre=usuario_nombre)
    
    if request.method == "POST":
        miFormulario = Usuario_nuevo_Formulario_vista (request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.email = informacion['email']
            usuario.password = informacion['password']

            usuario.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = Usuario_nuevo_Formulario(initial={'nombre': usuario.nombre, 'email':usuario.email , 
                                                         'password':usuario.password})
    return render(request, 'editarUsuarios.html', {'miFormulario':miFormulario, 'usuario_nombre':usuario_nombre})    