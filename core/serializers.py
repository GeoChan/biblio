from rest_framework import serializers
from . import models


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = ('url', 'codigo', 'email')


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Encuesta
        fields = ('url', 'enunciado', 'encuesta')


class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = serializers.HyperlinkedRelatedField(many=True, view_name='pregunta-detail',
                                                    queryset=models.Pregunta.objects.all())

    class Meta:
        model = models.Encuesta
        fields = ('url', 'descripcion', 'preguntas')


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Periodo
        fields = ('url', 'descripcon', 'fechaInicio', 'fechaFin')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registro
        fields = ('url', 'pregunta', 'codigo', 'periodo', 'escala')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = ('url', 'nombre')


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Libro
        fields = ('url', 'libro', 'nombre', 'categoria')


class BusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Busqueda
        fields = ('url', 'libro', 'periodo')


class PrestamoSerializer(serializers.ModelSerializer):
    class Metal:
        model = models.Prestamo
        fields = ('url', 'libro', 'periodo', 'persona')
