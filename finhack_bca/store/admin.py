from django.contrib import admin

from guardian.admin import GuardedModelAdmin

import finhack_bca.utils.models
from finhack_bca.store import models


class StoreAdmin(GuardedModelAdmin):
    list_display = [
        'name',
        'domain',
        'balance_formatted'
    ]

    def balance_formatted(self, instance):
        return 'IDR {:,}'.format(instance.balance).replace(',', '.')

    balance_formatted.short_description = 'saldo'
    balance_formatted.admin_order_field = 'balance'


class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'latitude',
        'longitude'
    ]


admin.site.register(models.Store, StoreAdmin)
admin.site.register(finhack_bca.utils.models.Location, LocationAdmin)
