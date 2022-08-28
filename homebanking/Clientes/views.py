from django.shortcuts import render
from .models import Cliente, Empleado,Direccion
from .serializers import ClienteSerializer,CuentaSerializer,PrestamoSerializer,SucursalesSerializer,TarjetaSerializer,DireccionesSerializer
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from Prestamos.models import Sucursal
from Tarjetas.models import Tarjeta
from rest_framework import status 
from rest_framework.permissions import IsAdminUser

def index (request):
    return render (request, 'Clientes/template/Clientes/inicio.html')

class ClienteViewSet(viewsets.mixins.ListModelMixin,viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = ClienteSerializer
    def get_queryset(self):
        id = self.request.user.id
        return Cliente.objects.filter(user_id = id)

class CuentaViewSet(viewsets.mixins.ListModelMixin,viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CuentaSerializer
    def get_queryset(self):
        id = self.request.user.id
        cliente = Cliente.objects.filter(user_id = id) 
        try:
            cl_id = cliente[0].customer_id
            return Cuenta.objects.filter(customer_id = cl_id)
        except:
            cuentas = []
            return cuentas

class PrestamoViewSet(viewsets.mixins.ListModelMixin,viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PrestamoSerializer
    def get_queryset(self):
        id = self.request.user.id
        cliente = Cliente.objects.filter(user_id = id)
        try:
            cl_id = cliente[0].customer_id
            return Prestamo.objects.filter(customer_id = cl_id)
        except:
            prestamos = []
            return prestamos


class PublicEndpoint(APIView):
    
    permission_classes = []

    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TarjetasViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = TarjetaSerializer
    def get_queryset(self):
        id = self.request.user.id
        empleado = Empleado.objects.filter(user_id = id)
        cliente_id = empleado[0].branch_id
        lista_clientes = Cliente.objects.filter(branch_id = cliente_id)
        lista = []
        tarjetas = Tarjeta.objects.all()
        for p in tarjetas:
            for c in lista_clientes:
                if p.customer_id == c.customer_id:
                    lista.append(p) 
        return lista 

class PublicEndpoint2(APIView):
    
    permission_classes = []

    def get(self, request):
        direcciones = Direccion.objects.all()
        serializer = DireccionesSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModificarBalanceViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()