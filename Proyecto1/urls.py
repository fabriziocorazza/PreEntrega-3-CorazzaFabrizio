"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import buscar_tareas, mostrar_tareas, cargar_tareas , mostrar_personas, cargar_personas, BuscarPersonas, mostrar_juegos, cargar_juegos, BuscarJuegos


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mis-tareas/", mostrar_tareas, name="tareas"),
    path("mis-tareas/cargar", cargar_tareas, name="tareas-create"),    
    path("mis-tareas/<busqueda>", buscar_tareas, name="tareas-list"),
    path("personas/", mostrar_personas, name="personas"),
    path("personas/create", cargar_personas, name="personas-create"),
    path('personas/lista', BuscarPersonas.as_view(), name="personas-list"),
    path("juegos/", mostrar_juegos , name="juegos"),
    path("juegos/create", cargar_juegos , name="juegos-create"),
    path('juegos/lista', BuscarJuegos.as_view(), name="juegos-list"), 

]
