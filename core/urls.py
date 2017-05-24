from rest_framework import routers
from django.conf.urls import url, include
from core.views import PeriodoViewSet, EncuestaViewSet, \
    PreguntaViewSet, PersonaViewSet, RegistroViewSet, \
    CategoriaViewSet, LibroViewSet, BusquedaViewSet, \
    PrestamoViewSet, UserViewSet, EncuestaActivaViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'encuesta', EncuestaViewSet)
router.register(r'encuesta_activa', EncuestaActivaViewSet, base_name='encuesta_activa')
router.register(r'pregunta', PreguntaViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'registro', RegistroViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'libro', LibroViewSet)
router.register(r'busqueda', BusquedaViewSet)
router.register(r'prestamo', PrestamoViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
