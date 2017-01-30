from rest_framework import routers
from django.conf.urls import url, include
from core.views import PeriodoViewSet, EncuestaViewSet, \
    PreguntaViewSet, PersonaViewSet, RegistroViewSet, \
    CategoriaViewSet, LibroViewSet, BusquedaViewSet, \
    PrestamoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'encuesta', EncuestaViewSet)
router.register(r'pregunta', PreguntaViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'registro', RegistroViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'libro', LibroViewSet)
router.register(r'Busqueda', BusquedaViewSet)
router.register(r'prestamo', PrestamoViewSet)
router.register(r'usuario', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
