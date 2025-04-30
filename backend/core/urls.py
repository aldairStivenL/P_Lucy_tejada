from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, CursoViewSet, InscripcionViewSet

# Router para las APIs
router = DefaultRouter()
router.register(r'users', UserViewSet)          # Rutas para usuarios
router.register(r'cursos', CursoViewSet)        # Rutas para cursos
router.register(r'inscripciones', InscripcionViewSet)  # Rutas para inscripciones

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas del router

    # Rutas de autenticación JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]