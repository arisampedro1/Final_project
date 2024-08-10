from django.utils import timezone
from django.db import models

# Create your models here.
from django.db import models
from datetime import timedelta
from django.utils import timezone

class Experiencia(models.Model):
    TIPOS_DE_EXPERIENCIA = [
        ('coaching', 'Coaching'),
        ('entrenamientos', 'Entrenamientos'),
        ('dinamicas', 'Dinámicas'),
    ]

    nombre = models.CharField(max_length=40, choices=TIPOS_DE_EXPERIENCIA)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    duracion = models.DurationField(blank=True, null=True)
    camada = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.get_nombre_display()


class Aprendiz(models.Model):
    NIVELES_DE_APRENDIZAJE = [
        ('iniciado', 'Iniciado'),
        ('aprendiz', 'Aprendiz'),
        ('alquimista', 'Alquimista'),
    ]

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    experiencia = models.CharField(max_length=40)
    nivel = models.CharField(max_length=10, choices=NIVELES_DE_APRENDIZAJE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.experiencia} {self.nivel}"


class Mentor(models.Model):
    EXPERIENCIA_NIVELES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('experto', 'Experto'),
    ]
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    experiencia = models.CharField(max_length=10, choices=EXPERIENCIA_NIVELES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    nivel = models.ForeignKey('NivelDeAprendizaje', on_delete=models.CASCADE, related_name='actividades')  # Si decides tener un modelo separado para niveles de aprendizaje
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE, related_name='actividades')
    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE, related_name='actividades')

    def __str__(self):
        return self.nombre


class NivelDeAprendizaje(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional del nivel
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Fecha en que se creó el nivel
    activo = models.BooleanField(default=True)  # Indica si el nivel está activo

    def __str__(self):
        return self.nombre