from rest_framework import serializers
from healthy_finance.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'nu_cliente',
            'rfc',
            'nombre_razon_social',
            'hashkey_casfim',
            'celular',
            'telefono',
            'telefono_credentials',
            'celular_credentials'
        )