from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

ESCALAS = (
    ('1', 'Si'),
    ('2', 'No'),
)


class Persona(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.codigo


class Encuesta(models.Model):
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return self.descripcion


class Pregunta(models.Model):
    enunciado = models.CharField(max_length=128)
    encuesta = models.ForeignKey(Encuesta, related_name='preguntas')

    def __str__(self):
        return self.enunciado


class Periodo(models.Model):
    descripcion = models.CharField(max_length=128)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.descripcion

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError('La fecha de inicio debe ser menor que la fecha final.')

    @staticmethod
    def activo():
        periodo = Periodo.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now()).first()
        if periodo is None:
            return -1
        return periodo.id


class Registro(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    codigo = models.ForeignKey(Persona)
    periodo = models.ForeignKey(Periodo)
    escala = models.CharField(max_length=128, choices=ESCALAS)

    def __str__(self):
        return self.escala

    class Meta:
        unique_together = ('pregunta', 'codigo', 'periodo',)


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
        return '%s, %s, %s' % (self.libro, self.persona, self.periodo,)
