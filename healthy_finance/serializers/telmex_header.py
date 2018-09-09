from rest_framework import serializers
from healthy_finance.models import TelmexHeader


class TelmexHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelmexHeader
        fields = (
            'uuid',
            'nocertificado',
            'blank',
            'certificado',
            'sello',
            'version',
            'fecha',
            'formapago',
            'subtotal',
            'descuento',
            'total',
            'metodopago',
            'lugarexpedicion',
            'moneda',
            'tipodecomprobante',
            'emisor_rfc',
            'receptor_rfc'
        )