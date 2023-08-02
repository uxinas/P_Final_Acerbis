from django import forms


class LoginFormulario(forms.Form):
    nombre = forms.CharField ()
    email = forms.CharField () 
    password = forms.CharField () 