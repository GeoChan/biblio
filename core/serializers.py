from rest_framework import serializers
from core.models import Persona, Periodo, Busqueda, Categoria, Registro, Encuesta, Libro, Prestamo, Pregunta
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class RegistroPersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ('pregunta', 'periodo')


class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('url', 'enunciado', 'encuesta')


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    registros = serializers.SerializerMethodField()

    def get_registros(self, persona):
        queryset = Registro.objects.filter(persona=persona, periodo__activo=True)
        serializer = RegistroPersonaSerializer(instance=queryset, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = Persona
        fields = ('url', 'codigo', 'email', 'registros', 'completado', 'completado_encuesta')


class PreguntaRelatedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('url', 'enunciado')


class EncuestaSerializer(serializers.HyperlinkedModelSerializer):
    preguntas = PreguntaRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ('url', 'descripcion', 'preguntas', 'periodos')


class EncuestaActivaSerializer(serializers.HyperlinkedModelSerializer):
    preguntas = PreguntaRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ('url', 'descripcion', 'preguntas', 'cobertura', 'cobertura_respuesta', 'periodos', 'reporte_mejora')


class PeriodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Periodo
        fields = ('url', 'descripcion', 'fecha_inicio', 'fecha_fin', 'activo', 'encuestas')

    def validate(self, attrs):
        if attrs['fecha_inicio'] > attrs['fecha_fin']:
            raise ValidationError({
                'fecha_inicio': 'debe ser menor o igual que la fecha final',
                'fecha_fin': 'debe ser mayor o igual de la fecha inicial'
            })
        return attrs


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ('url', 'pregunta', 'persona', 'periodo', 'escala')


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
