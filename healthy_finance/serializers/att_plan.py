from rest_framework import serializers
from healthy_finance.models import AttPlan


class AttPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttPlan
        fields = (
          'hashkey',
          'plan',
          'cuenta',
          'renta',
          'plazo',
          'meses',
          'fin',
        )