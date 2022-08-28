
from email.mime import base
from django.urls import path, include

from . import views
from Prestamos.views import SucursalViewSet, SolicitudPrestamoViewSet, ModificarDireccionesViewSet, ModificarMiDireccionViewSet
from rest_framework.routers import DefaultRouter
from .views import ModificarBalanceViewSet, PublicEndpoint,PublicEndpoint2

router = DefaultRouter()
router.register(r'Informacion del cliente',views.ClienteViewSet, basename='cl')
router.register(r'Informacion de cuentas',views.CuentaViewSet, basename='cu')
router.register(r'Prestamos del cliente',views.PrestamoViewSet, basename='pr')
router.register(r'Prestamos por sucursal',SucursalViewSet, basename='su')
router.register(r'Tarjetas del cliente ', views.TarjetasViewSet, basename='tj')
router.register(r'Solicitar y eliminar prestamos', SolicitudPrestamoViewSet, basename='sp')
router.register(r'Modificar direcciones', ModificarDireccionesViewSet, basename='md')
router.register(r'Modificar mi direccion como cliente', ModificarMiDireccionViewSet, basename='mi')
router.register(r'Modificar balance del cliente', ModificarBalanceViewSet, basename='mb')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls), name = 'api'),
    path('api/sucursales/',PublicEndpoint.as_view()),
    path('api/direcciones/',PublicEndpoint2.as_view()),
]