from django import forms

class Usuario_nuevo_Formulario(forms.Form):
    nombre = forms.CharField ()
    email = forms.CharField () 
    password = forms.CharField () 