
from email.mime import base
from django.urls import path, include

from . import views
from Prestamos.views import SucursalViewSet, SolicitudPrestamoViewSet, ModificarDireccionesViewSet, ModificarMiDireccionViewSet
from rest_framework.routers import DefaultRouter
from .views import ModificarBalanceViewSet, PublicEndpoint

router = DefaultRouter()
router.register(r'informacion_del_cliente',views.ClienteViewSet, basename='cl')
router.register(r'informacion_de_cuentas',views.CuentaViewSet, basename='cu')
router.register(r'prestamos_del_cliente',views.PrestamoViewSet, basename='pr')
router.register(r'prestamos_por_sucursal/(?P<id>\d+)',SucursalViewSet, basename='su')
router.register(r'listas_de_clientes ', views.ClientesViewSet, basename='ls')
router.register(r'tarjetas/(?P<id>\d+)', views.TarjetasViewSet, basename='tj')
router.register(r'solicitar_y_eliminar_prestamos', SolicitudPrestamoViewSet, basename='sp')
router.register(r'modificar_direcciones', ModificarDireccionesViewSet, basename='md')
router.register(r'modificar_mi direccion_como_cliente', ModificarMiDireccionViewSet, basename='mi')
router.register(r'modificar_balance_del_cliente', ModificarBalanceViewSet, basename='mb')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls), name = 'api'),
    path('api/sucursales/',PublicEndpoint.as_view()),
]