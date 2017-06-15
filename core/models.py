from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# from django.db.models import Q

ESCALAS = (
    ('1', 'Si'),
    ('2', 'No'),
)


class Persona(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    email = models.EmailField(null=True, blank=True)
    preguntas = models.ManyToManyField('Pregunta', through='Registro')

    def __str__(self):
        return self.codigo

    @property
    def completado(self):
        periodo = Periodo.get_activo()
        if periodo is None:
            return 'no hay periodo activo'
        preguntas = Pregunta.objects.filter(encuesta__in=list(periodo.encuestas.all())).all()
        preguntas_contestadas = Registro.objects.filter(
            pregunta__in=list(preguntas),
            persona=self,
            periodo=periodo
        ).count()
        total_preguntas = len(preguntas)
        if total_preguntas == 0:
            return 100.0
        return preguntas_contestadas / total_preguntas * 100.0

    @property
    def completado_encuesta(self):
        periodo = Periodo.get_activo()
        if periodo is None:
            return 'no ha periodo activo'
        encuestas = periodo.encuestas.all()
        resultado = []
        for encuesta in encuestas:
            preguntas = Pregunta.objects.filter(encuesta=encuesta).all()
            preguntas_contestadas = Registro.objects.filter(
                pregunta__in=list(preguntas),
                persona=self,
                periodo=periodo
            ).count()
            total_preguntas = len(preguntas)
            if total_preguntas == 0:
                return 100.0
            porcentaje = preguntas_contestadas / total_preguntas * 100.0
            resultado.append({
                'descripcion': encuesta.descripcion,
                'porcentaje': porcentaje,
                'total_preguntas': total_preguntas,
                'preguntas_contestadas': preguntas_contestadas
            })
        return resultado


class Encuesta(models.Model):
    descripcion = models.CharField(max_length=128)
    periodos = models.ManyToManyField('Periodo', related_name='encuestas')

    def __str__(self):
        return self.descripcion

    @property
    def cobertura(self):
        total_preguntas = Persona.objects.count() * self.preguntas.count()
        total_respuestas = Registro.objects.filter(
            pregunta__in=list(self.preguntas.all()),
            periodo=Periodo.get_activo()
        ).count()
        if total_preguntas == 0:
            return 100.0
        return total_respuestas / total_preguntas * 100

    @property
    def cobertura_respuesta(self):
        respuestas = Registro.objects.filter(pregunta__in=list(self.preguntas.all()), periodo=Periodo.get_activo())
        resultado = {}
        for pregunta in self.preguntas.all().order_by('pk'):
            resultado[pregunta.id] = {
                'enunciado': pregunta.enunciado,
                'escala': {clave: 0 for _, clave in ESCALAS}
            }
        for respuesta in respuestas:
            key = ''
            for value, escala in ESCALAS:
                if value == respuesta.escala:
                    key = escala
            if key in resultado[pregunta.id]['escala']:
                resultado[respuesta.pregunta_id]['escala'][key] += 1
        return [value for _, value in resultado.items()]


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
    activo = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s - %s) %s" % (
            self.descripcion, self.fecha_inicio, self.fecha_fin, 'activo' if self.activo else ''
        )

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError({
                'fecha_inicio': 'debe ser menor o igual que la fecha final',
                'fecha_fin': 'debe ser mayor o igual de la fecha inicial'
            })

    def save(self, *args, **kwargs):
        if self.activo:
            if self.pk is None:
                Periodo.objects.update(activo=False)
            else:
                Periodo.objects.exclude(pk=self.pk).update(activo=False)
        super(Periodo, self).save(*args, **kwargs)

    @staticmethod
    def get_actual():
        return Periodo.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now()).first()

    @staticmethod
    def get_activo():
        return Periodo.objects.filter(activo=True).first()


class Registro(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas')
    persona = models.ForeignKey(Persona, related_name='respuestas')
    periodo = models.ForeignKey(Periodo, related_name='respuestas')
    escala = models.CharField(max_length=128, choices=ESCALAS)

    def __str__(self):
        return "%s - %s: %s = %s" % (self.periodo, self.persona, self.pregunta, self.escala)

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
