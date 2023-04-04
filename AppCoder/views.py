from django.shortcuts import render
from AppCoder.models import Tarea, Persona, Juegos
from AppCoder.forms import PersonaForm,BuscarPersonasForm, TareaForm, JuegosForm, BuscarJuegosForm
from django.views.generic import ListView

## MODELO DE TAREAS

def mostrar_tareas (request):
    tareas = Tarea.objects.all()
    total_tareas = len(tareas)
    context = {"tareas": tareas, "total_tareas": total_tareas, "form": TareaForm(),}
    return render(request, "AppCoder/tarea.html", context)

def buscar_tareas (request, busqueda):
    if busqueda == "todo":
        tareas = Tarea.objects.all()
    else:
        tareas = Tarea.objects.filter(nombre=busqueda).all()
    
    return render(request, "AppCoder/tarea.html", {"tareas": tareas})

def cargar_tareas (request):
    f = TareaForm(request.POST)    
    context = {
        "form": f
    }

    if f.is_valid(): 
        Tarea(nombre=f.data["nombre"]).save()
        context["form"] = TareaForm()
    
    context["tareas"] = Tarea.objects.all()
    context["total_tareas"] = len(Tarea.objects.all())
    
    return render(request, "AppCoder/tarea.html", context)

## MODELO DE PERSONA

def mostrar_personas(request):

    persona = Persona.objects.all()
    total_personas = len(persona)
    context = {"persona": persona, "total_personas": total_personas, "form": PersonaForm(),}
    return render (request, "AppCoder/personas.html", context)

def cargar_personas(request):
    f = PersonaForm(request.POST)    
    context = {
        "form": f
    }

    if f.is_valid(): 
        Persona(nombre=f.data["nombre"],
        apellido=f.data["apellido"],
        fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context["form"] = PersonaForm()
    
    context["persona"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
    
    return render(request, "AppCoder/personas.html", context)


class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "persona"
    
    
    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()

## MODELO JUEGOS
def mostrar_juegos(request):

    juego = Juegos.objects.all()
    total_juegos = len(juego)
    context = {"juego": juego, "total_juegos": total_juegos, "form": JuegosForm(),}
    return render (request, "AppCoder/juegos.html", context)

def cargar_juegos(request):
    f = JuegosForm(request.POST)    
    context = {
        "form": f
    }

    if f.is_valid(): 
        Juegos(nombre=f.data["nombre"],
        descripcion=f.data["descripcion"]).save()
        context["form"] = JuegosForm()
    
    context["Juegos"] = Juegos.objects.all()
    context["total_juegos"] = len(Juegos.objects.all())
    
    return render(request, "AppCoder/juegos.html", context)


class BuscarJuegos(ListView):
    model = Juegos
    context_object_name = "juego"
    
    
    def get_queryset(self):
        f = BuscarJuegosForm(self.request.GET)
        if f.is_valid():
            return Juegos.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Juegos.objects.none()
