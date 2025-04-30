from django.contrib import admin
from .models import User, Curso, Inscripcion

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'telefono', 'genero')
    search_fields = ('username', 'email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horario', 'cupo_maximo', 'formador')
    list_filter = ('formador',)
    search_fields = ('nombre',)

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'calificacion')
    list_filter = ('curso',)
    search_fields = ('estudiante__username', 'curso__nombre')