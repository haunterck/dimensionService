from rest_framework import serializers
from healthy_finance.models import LuIeps


class LuIepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuIeps
        fields = (
            'hashkey',
            'descripcion',
            'porcentaje',
            'is_active'
        )
