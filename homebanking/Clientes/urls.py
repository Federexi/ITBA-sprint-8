
from django.urls import path, include

from . import views
from Prestamos.views import SucursalViewSet
#from Tarjetas.views import TarjetasViewSet
from rest_framework.routers import DefaultRouter
from .views import PublicEndpoint

router = DefaultRouter()
router.register(r'cliente',views.ClienteViewSet, basename='cl')
router.register(r'cuentas',views.CuentaViewSet, basename='cu')
router.register(r'prestamos',views.PrestamoViewSet, basename='pr')
router.register(r'sucursal',SucursalViewSet, basename='su')
#router.register(r'tarjetas',TarjetasViewSet, basename='tj')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls), name = 'api'),
    path('api/sucursales/',PublicEndpoint.as_view()),
]