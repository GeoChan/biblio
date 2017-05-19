from core.models import Periodo, Persona, Encuesta, Pregunta, Registro, Categoria, Libro, Busqueda, Prestamo
from core.serializers import PeriodoSerializer, PersonaSerializer, EncuestaSerializer, RegistroSerializer, \
    CategoriaSerializer, LibroSerializer, BusquedaSerializer, PrestamoSerializer, UserSerializer, PreguntaSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import mixins


class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()


class EncuestaViewSet(viewsets.ModelViewSet):
    serializer_class = EncuestaSerializer
    queryset = Encuesta.objects.all().prefetch_related('preguntas')


class PreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PreguntaSerializer
    queryset = Pregunta.objects.all()


class PeriodoViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodoSerializer
    queryset = Periodo.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current':
            kwargs['pk'] = Periodo.activo()
        return super(PeriodoViewSet, self).dispatch(request, *args, **kwargs)


class RegistroViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()


class BusquedaViewSet(viewsets.ModelViewSet):
    serializer_class = BusquedaSerializer
    queryset = Busqueda.objects.all()


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current' and request.user:
            kwargs['pk'] = request.user.pk
        return super(UserViewSet, self).dispatch(request, *args, **kwargs)


def home(request):
    if request.user.is_authenticated:
        return redirect('/board/index.html')
    return redirect('/login')
