from rest_framework import serializers
from core.models import Persona, Periodo, Busqueda, Categoria, Registro, Encuesta, Libro, Prestamo, Pregunta


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('url', 'codigo', 'email')


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('url', 'enunciado', 'encuesta')


class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ('url', 'descripcion', 'preguntas')


class PeriodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periodo
        fields = ('url', 'descripcion', 'fechaInicio', 'fechaFin')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('url', 'pregunta', 'codigo', 'periodo', 'escala')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre')


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('url', 'libro', 'nombre', 'categoria')


class BusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busqueda
        fields = ('url', 'libro', 'periodo')


class PrestamoSerializer(serializers.ModelSerializer):
    class Metal:
        model = Prestamo
        fields = ('url', 'libro', 'periodo', 'persona')
