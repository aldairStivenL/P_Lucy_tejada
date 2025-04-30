from django.db import models
from django.contrib.auth.models import AbstractUser

# Opciones para roles y género
ROLES = (
    ('admin', 'Administrador'),
    ('formador', 'Formador'),
    ('estudiante', 'Estudiante'),
)

GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Modelo personalizado de usuario
class User(AbstractUser):
    rol = models.CharField(max_length=10, choices=ROLES, default='estudiante')  # Agregamos un valor predeterminado
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Permitimos null en la base de datos
    genero = models.CharField(max_length=1, choices=GENERO, blank=True, null=True)  # Permitimos null en la base de datos

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

# Modelo para los cursos
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100, help_text="Ejemplo: Lunes y Miércoles, 4:00 PM - 6:00 PM")
    cupo_maximo = models.PositiveIntegerField(help_text="Número máximo de estudiantes permitidos")
    formador = models.ForeignKey(
        User,
        limit_choices_to={'rol': 'formador'},
        on_delete=models.SET_NULL,
        null=True,
        related_name='cursos_impartidos'  # Mejora la relación inversa
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

# Modelo para las inscripciones
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        User,
        limit_choices_to={'rol': 'estudiante'},
        on_delete=models.CASCADE,
        related_name='inscripciones'  # Mejora la relación inversa
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscritos'  # Mejora la relación inversa
    )
    asistencia = models.JSONField(default=list, help_text="Lista de fechas de asistencia (formato: ['YYYY-MM-DD', ...])")
    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Calificación final del estudiante (ejemplo: 4.5)"
    )

    def __str__(self):
        return f"{self.estudiante.username} en {self.curso.nombre}"

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"

#####coment
#####coment