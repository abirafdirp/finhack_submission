from django.contrib import admin

from finhack_bca.store import models


class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'domain',
        'balance_formatted'
    ]

    def balance_formatted(self, instance):
        return 'IDR {:,}'.format(instance.balance).replace(',', '.')

    balance_formatted.short_description = 'saldo'
    balance_formatted.admin_order_field = 'balance'


admin.site.register(models.Store, StoreAdmin)