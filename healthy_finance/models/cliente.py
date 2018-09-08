# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nu_cliente = models.CharField(max_length=12, primary_key=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    nombre_razon_social = models.CharField(max_length=96, blank=True, null=True)
    hashkey_casfim = models.ForeignKey('LuCasfim', models.DO_NOTHING, db_column='hashkey_casfim', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'