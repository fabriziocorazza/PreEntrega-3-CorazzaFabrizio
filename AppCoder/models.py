from django.db import models

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100, default="por hacer")
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    def terminar(self):
        self.estado = "Terminado"
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    

class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"
    
class Juegos(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.id} - {self.nombre}  --- {self.descripcion}"




