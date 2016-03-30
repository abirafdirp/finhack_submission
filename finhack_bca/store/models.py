from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Store(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    domain = models.URLField()
    short_description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Toko'
        verbose_name_plural = 'Toko'
        permissions = (
            ('view_store', 'Can view store'),
        )


@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()