from django.db import models

class Bancomerpay(models.Model):
    hashkey = models.CharField(primary_key=True, max_length=96)
    ot = models.CharField(max_length=4, blank=True, null=True)
    alias = models.CharField(max_length=10, blank=True, null=True)
    cl = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    rern = models.CharField(max_length=7, blank=True, null=True)
    refa = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bank = models.CharField(max_length=24, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    qr = models.CharField(max_length=500, blank=True, null=True)
    pagado = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancomerpay'