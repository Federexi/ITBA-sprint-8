from Clientes.models import Empleado
from .models import Prestamo

from rest_framework import serializers

class SucursalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_type', 'loan_total', 'customer_id', 'loan_date']



