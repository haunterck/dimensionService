from django.db import models


class Profile(models.Model):
    nu_cliente = models.CharField(primary_key=True, max_length=96)
    rfc = models.TextField(blank=True, null=True)
    nombre_razon_social = models.TextField(blank=True, null=True)
    hashkey_casfim = models.IntegerField()
    celular = models.CharField(max_length=24, blank=True, null=True)
    telefono = models.CharField(max_length=24, blank=True, null=True)
    telefono_credentials = models.CharField(max_length=24, blank=True, null=True)
    celular_credentials = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'