from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Curso, Inscripcion

# Obtener el modelo de usuario personalizado
User = get_user_model()

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol', 'telefono', 'genero']

# Serializador para el modelo Curso
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'horario', 'cupo_maximo', 'formador']

# Serializador para el modelo Inscripcion
class InscripcionSerializer(serializers.ModelSerializer):
    estudiante = serializers.StringRelatedField()  # Muestra el nombre del estudiante
    curso = serializers.StringRelatedField()       # Muestra el nombre del curso

    class Meta:
        model = Inscripcion
        fields = ['id', 'estudiante', 'curso', 'asistencia', 'calificacion']