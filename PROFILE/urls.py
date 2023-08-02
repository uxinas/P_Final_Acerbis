from django.urls import path
from PROFILE import views




urlpatterns = [
    
    path('perfiles', views.profile, name='perfiles'),
    path('busquedaPerfiles', views.busquedaPerfiles, name='busquedaPerfiles'),
    

    ]