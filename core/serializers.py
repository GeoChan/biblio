from rest_framework import serializers
from core.models import Persona, Periodo, Busqueda, Categoria, Registro, Encuesta, Libro, Prestamo, Pregunta
from django.contrib.auth.models import User


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('url', 'codigo', 'email')


class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('url', 'enunciado', 'encuesta')


class PreguntaRelatedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('url', 'enunciado')


class EncuestaSerializer(serializers.HyperlinkedModelSerializer):
    preguntas = PreguntaRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ('url', 'descripcion', 'preguntas')


class PeriodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Periodo
        fields = ('url', 'descripcion', 'fecha_inicio', 'fecha_fin')

    def validate(self, attrs):
        Periodo(**attrs).clean()
        return attrs


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ('url', 'pregunta', 'codigo', 'periodo', 'escala')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre')


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('url', 'libro', 'nombre', 'categoria')


class BusquedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Busqueda
        fields = ('url', 'libro', 'periodo')


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('url', 'libro', 'periodo', 'persona')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')
