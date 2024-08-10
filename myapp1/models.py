from datetime import timezone
from django.db import models

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
    nivel = models.CharField(max_length=30)  # Cambiado de ForeignKey a CharField
    experiencia = models.CharField(max_length=40)  # Cambiado de ForeignKey a CharField
    aprendiz = models.CharField(max_length=40, blank=True, null=True)  # Cambiado de ForeignKey a CharField

    def __str__(self):
        return self.nombre


class NivelDeAprendizaje(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional del nivel
    fecha_creacion = models.DateTimeField(default=timezone)  # Fecha en que se creó el nivel
    activo = models.BooleanField(default=True)  # Indica si el nivel está activo

    def __str__(self):
        return self.nombre