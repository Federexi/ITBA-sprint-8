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


class ClientesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ['customer_id','customer_name', 'customer_surname']  


class TarjetaSerializer(serializers.ModelSerializer):
    customer_id = serializers.ReadOnlyField(source='customer_id.customer_id')
    class Meta:
        model = Tarjeta
        fields = ['customer_id','card_id','card_type','card_number', 'cvv', ]  


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"    

class MiDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['address_id', 'address', 'postal_zip', 'city', 'state', 'country']