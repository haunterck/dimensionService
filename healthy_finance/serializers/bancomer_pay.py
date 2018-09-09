from rest_framework import serializers
from healthy_finance.models import Bancomerpay

class BancomerpaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bancomerpay
        fields = (
          'hashkey',
          'ot',
          'alias',
          'cl',
          'type',
          'rern',
          'refa',
          'amount',
          'bank',
          'country',
          'currency',
          'qr',
          'pagado',
          'periodo',
        )