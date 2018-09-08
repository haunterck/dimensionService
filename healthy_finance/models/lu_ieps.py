from django.db import models


class LuIeps(models.Model):
    hashkey = models.CharField(primary_key=True, max_length=96, db_column='hashkey')
    descripcion = models.CharField(max_length=96, blank=True, null=True)
    porcentaje = models.CharField(max_length=24, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lu_ieps'
