from rest_framework import serializers
from healthy_finance.models import LuCasfim


class LuCasfimSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuCasfim
        fields = (
          'hashkey',
          'sector',
          'actividad',
          'is_active',
        )