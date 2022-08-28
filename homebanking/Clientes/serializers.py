from rest_framework import serializers

from Prestamos.models import Sucursal
from .models import Cliente, Direccion,TipoCliente
from django.contrib.auth.models import User
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjeta

class TipoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCliente
        fields = ['cu_type']
               
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    
    customer_type = TipoClienteSerializer()
    

    class Meta:
        model = Cliente
        fields = ['customer_id', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch_id', 'customer_type']


class CuentaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cuenta
        fields = ['account_id', 'balance', 'type']


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_type', 'loan_total']


class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"        


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tarjeta
        fields = '__all__'

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"    