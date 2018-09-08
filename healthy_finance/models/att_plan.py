from django.db import models


class AttPlan(models.Model):
    hashkey = models.CharField(primary_key=True, max_length=96)
    plan = models.CharField(max_length=30, blank=True, null=True)
    cuenta = models.IntegerField(blank=True, null=True)
    renta = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    plazo = models.CharField(max_length=72, blank=True, null=True)
    meses = models.CharField(max_length=72, blank=True, null=True)
    fin = models.CharField(max_length=72, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_plan'
