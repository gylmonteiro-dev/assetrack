from django.db import models



MOVABLE_OR_IMMOVABLE = (('M', 'MOVÉL'),
                   ('I', 'IMÓVEL'))


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name='Modelo')
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='Número de série')
    price = 

