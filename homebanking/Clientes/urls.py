
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cliente',views.ClienteViewSet, basename='cl')
router.register(r'cuentas',views.CuentaViewSet, basename='cu')
router.register(r'prestamos',views.PrestamoViewSet, basename='pr')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls)),
]