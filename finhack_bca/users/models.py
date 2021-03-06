# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from guardian.mixins import GuardianUserMixin

from finhack_bca.store.models import Store


TYPE = (
    ('counter', 'Counter'),
    ('customer', 'Customer'),
    ('staff', 'Staff'),
    ('store', 'Store')
)


@python_2_unicode_compatible
class User(AbstractUser, GuardianUserMixin):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    type = models.CharField(choices=TYPE, blank=True, null=True, max_length=20)

    # this meant for counter only
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    balance = models.IntegerField(default=0)

    # for store only
    stores = models.ManyToManyField(Store, blank=True)

    # BCA's mandatory fields, email is used as primary id bca
    date_of_birth = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
