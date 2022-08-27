""" from Tarjetas.models import Tarjeta
from rest_framework import serializers


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tarjeta
        fields = ['__all__']  """