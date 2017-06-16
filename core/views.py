from core.models import Periodo, Persona, Encuesta, Pregunta, Registro, Categoria, Libro, Busqueda, Prestamo
from core.serializers import PeriodoSerializer, PersonaSerializer, EncuestaSerializer, RegistroSerializer, \
    CategoriaSerializer, LibroSerializer, BusquedaSerializer, PrestamoSerializer, UserSerializer, PreguntaSerializer, \
    EncuestaActivaSerializer
from rest_framework import viewsets, mixins, permissions, pagination, generics
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all().order_by('pk')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def dispatch(self, request, *args, **kwargs):
        if str(kwargs.get('pk'))[0:1] == 'c':
            persona = Persona.objects.filter(codigo=kwargs.get('pk')[1:]).first()
            kwargs['pk'] = -1 if persona is None else persona.id
        return super(PersonaViewSet, self).dispatch(request, *args, **kwargs)


class EncuestaViewSet(viewsets.ModelViewSet):
    serializer_class = EncuestaSerializer
    queryset = Encuesta.objects.all().prefetch_related('preguntas').order_by('pk')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EncuestaActivaViewSet(viewsets.ModelViewSet):
    serializer_class = EncuestaActivaSerializer
    queryset = Encuesta.objects.filter(periodos__activo=True).all().prefetch_related('preguntas').order_by('pk')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PreguntaSerializer
    queryset = Pregunta.objects.all().order_by('pk')


class PeriodoViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodoSerializer
    queryset = Periodo.objects.all().order_by('pk')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'active':
            periodo = Periodo.get_activo()
            kwargs['pk'] = -1 if periodo is None else periodo.id
        elif kwargs.get('pk') == 'current':
            periodo = Periodo.get_actual()
            kwargs['pk'] = -1 if periodo is None else periodo.id
        return super(PeriodoViewSet, self).dispatch(request, *args, **kwargs)


class RegistroViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all().order_by('pk')
    permission_classes = (permissions.AllowAny,)


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('pk')


class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all().order_by('pk')


class BusquedaViewSet(viewsets.ModelViewSet):
    serializer_class = BusquedaSerializer
    queryset = Busqueda.objects.all().order_by('pk')


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all().order_by('pk')


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('pk')

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current' and request.user:
            kwargs['pk'] = request.user.pk
        return super(UserViewSet, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request, 'index.html')
