
from django.urls import path, include

from . import views
from Prestamos.views import SucursalViewSet
from rest_framework.routers import DefaultRouter
from .views import PublicEndpoint

router = DefaultRouter()
router.register(r'Informacion del cliente',views.ClienteViewSet, basename='cl')
router.register(r'Informacion de cuentas',views.CuentaViewSet, basename='cu')
router.register(r'Prestamos del cliente',views.PrestamoViewSet, basename='pr')
router.register(r'Prestamos por sucursal',SucursalViewSet, basename='su')
router.register(r'Tarjetas del cliente ', views.TarjetasViewSet, basename='tj')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls), name = 'api'),
    path('api/sucursales/',PublicEndpoint.as_view()),
]