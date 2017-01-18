from django.db import models

ESCALAS = (
    ('1', 'Totalmente en desacuerdo'),
    ('2', 'En desacuerdo'),
    ('3', 'Ni acuerdo ni desacuerdo'),
    ('4', 'De acuerdo'),
    ('5', 'Totalmente de acuerdo')
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
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return self.descripcion


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
        return '%s, %s, %s' % (self.libro, self.persona, self.periodo)
