from . import models, serializers
from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.pagination import PageNumberPagination


class PaginationControl(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 1000


class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonaSerializer
    queryset = models.Persona.objects.all()
    pagination_class = PaginationControl


class EncuestaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EncuestaSerializer
    queryset = models.Encuesta.objects.all()


class PreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PreguntaSerializer
    queryset = models.Pregunta.objects.all()


class PeriodoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PeriodoSerializer
    queryset = models.Periodo.objects.all()


class RegistroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroSerializer
    queryset = models.Registro.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroSerializer
    queryset = models.Categoria.objects.all()


class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroSerializer
    queryset = models.Libro.objects.all()


class BusquedaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroSerializer
    queryset = models.Busqueda.objects.all()


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroSerializer
    queryset = models.Prestamo.objects.all()


def home(request):
    if request.user.is_authenticated:
        return redirect('/board/index.html')
    return redirect('/login')
