from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Q

ESCALAS = (
    ('1', 'Si'),
    ('2', 'No'),
)


class Persona(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    email = models.EmailField()
    preguntas = models.ManyToManyField('Pregunta', through='Registro')

    def __str__(self):
        return self.codigo


class Encuesta(models.Model):
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return self.descripcion


class Pregunta(models.Model):
    enunciado = models.CharField(max_length=256)
    encuesta = models.ForeignKey(Encuesta, related_name='preguntas')
    personas = models.ManyToManyField('Persona', through='Registro')

    def __str__(self):
        return self.enunciado


class Periodo(models.Model):
    descripcion = models.CharField(max_length=128)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    personas = models.ManyToManyField('Persona', through='Registro')

    def __str__(self):
        return "%s (%s - %s)" % (self.descripcion, self.fecha_inicio, self.fecha_fin)

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError({
                'fecha_inicio': 'debe ser menor o igual que la fecha final',
                'fecha_fin': 'debe ser mayor o igual de la fecha inicial'
            })

    @staticmethod
    def activo():
        periodo = Periodo.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now()).first()
        return periodo


class Registro(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas')
    persona = models.ForeignKey(Persona, related_name='respuestas')
    periodo = models.ForeignKey(Periodo, related_name='respuestas')
    escala = models.CharField(max_length=128, choices=ESCALAS)

    def __str__(self):
        return "%d - %s: %s = $s" % (self.periodo, self.persona, self.pregunta, self.escala)

    class Meta:
        unique_together = ('pregunta', 'persona', 'periodo')


class Categoria(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    libro = models.CharField(max_length=8)
    nombre = models.CharField(max_length=128)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return self.libro


class Busqueda(models.Model):
    libro = models.ForeignKey(Libro)
    periodo = models.ForeignKey(Periodo)

    def __str__(self):
        return '%s' % self.libro


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro)
    periodo = models.ForeignKey(Periodo)
    persona = models.ForeignKey(Persona)

    def __str__(self):
        return '%s, %s, %s' % (self.libro, self.persona, self.periodo)
