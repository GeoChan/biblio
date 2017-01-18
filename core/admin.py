from django.contrib import admin
from . import models
admin.site.register(models.Encuesta)
admin.site.register(models.Periodo)
admin.site.register(models.Persona)
admin.site.register(models.Pregunta)
admin.site.register(models.Registro)
admin.site.register(models.Categoria)
admin.site.register(models.Libro)
admin.site.register(models.Busqueda)
admin.site.register(models.Prestamo)

# Register your models here.
