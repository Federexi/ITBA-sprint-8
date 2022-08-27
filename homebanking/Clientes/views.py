from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer,CuentaSerializer,PrestamoSerializer,SucursalesSerializer
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from Prestamos.models import Sucursal
from rest_framework import status 

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