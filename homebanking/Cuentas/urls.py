
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'cuentas',views.CuentaViewSet, basename='cu')

urlpatterns = [
    path('actividad/',views.act, name = 'act'),
    path('configuracion/', views.conf, name = 'conf'),
    path('',  views.hub, name = 'hub'),
    path('inversiones/', views.inv, name = 'inv'),
    path('seguridad/', views.seg, name = 'seg'),
    path('transferencias/', views.transf, name = 'transf'),
    # path('api/', include(router.urls))
]