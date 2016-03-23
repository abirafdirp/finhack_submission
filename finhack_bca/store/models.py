from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    domain = models.URLField()
    short_description = models.CharField(max_length=255)
