from rest_framework import serializers
from healthy_finance.models import Cliente
from healthy_finance.models import LuCasfim

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
          'nu_cliente',
          'rfc',
          'nombre_razon_social',
          'hashkey_casfim',
        )