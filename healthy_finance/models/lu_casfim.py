from django.db import models


class LuCasfim(models.Model):
    hashkey = models.CharField(primary_key=True, max_length=96)
    sector = models.CharField(max_length=72, blank=True, null=True)
    actividad = models.CharField(max_length=72, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lu_casfim'
