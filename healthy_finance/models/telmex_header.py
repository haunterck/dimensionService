from django.db import models

class TelmexHeader(models.Model):
    uuid = models.CharField(primary_key=True, max_length=72)
    nocertificado = models.TextField(db_column='noCertificado', blank=True, null=True)  # Field name made lowercase.
    certificado = models.TextField(blank=True, null=True)
    sello = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    fecha = models.TextField(blank=True, null=True)
    formapago = models.TextField(db_column='formaPago', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.TextField(db_column='subTotal', blank=True, null=True)  # Field name made lowercase.
    descuento = models.TextField(blank=True, null=True)
    total = models.TextField(blank=True, null=True)
    metodopago = models.TextField(blank=True, null=True)
    lugarexpedicion = models.TextField(blank=True, null=True)
    moneda = models.TextField(blank=True, null=True)
    tipodecomprobante = models.TextField(db_column='TipoDeComprobante', blank=True, null=True)  # Field name made lowercase.
    emisor_rfc = models.TextField(blank=True, null=True)
    receptor_rfc = models.TextField(db_column='receptor_Rfc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telmex_header'