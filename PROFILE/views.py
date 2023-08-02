from django.shortcuts import render
from SIGNUP.models import Usuario_nuevo


def profile(request):
    return render(request,'profile.html')


#def busquedaCamada(request):
   # return render(request, 'AppCoder/busquedaCamada.html')

def busquedaPerfiles(request):
    if request.GET['email']:


        email = request.GET['email']
        nombre = Usuario_nuevo.objects.filter(perfiles__icontains=email)

        return render(request, 'profile.html', {'email':email, 'nombre':nombre})
    
    else:
        respuesta = "No enviaste datos."


    return render(request, 'inicio.html', {'respuesta':respuesta})

