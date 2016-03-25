from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from finhack_bca.transaction import models


class CounterTopUpAdmin(GuardedModelAdmin):
    list_display = [
        'counter',
        'date',
        'amount_formatted',
        'status',
        'method'
    ]
    list_filter = [
        'date',
        'counter',
        'amount',
        'status',
        'method'
    ]

    def amount_formatted(self, instance):
        return 'IDR {:,}'.format(instance.amount).replace(',', '.')

    amount_formatted.short_description = 'jumlah'
    amount_formatted.admin_order_field = 'amount'


class CustomerTopUpAdmin(GuardedModelAdmin):
    list_display = [
        'customer',
        'date',
        'counter',
        'amount_formatted',
        'status'
    ]
    list_filter = [
        'customer',
        'date',
        'counter',
        'amount',
        'status'
    ]

    def amount_formatted(self, instance):
        return 'IDR {:,}'.format(instance.amount).replace(',', '.')

    amount_formatted.short_description = 'jumlah'
    amount_formatted.admin_order_field = 'amount'


class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date',
        'amount_formatted',
        'status'
    ]
    list_filter = [
        'user',
        'date',
        'amount',
        'status'
    ]

    def amount_formatted(self, instance):
        return 'IDR {:,}'.format(instance.amount).replace(',', '.')

    amount_formatted.short_description = 'jumlah'
    amount_formatted.admin_order_field = 'amount'


class TransactionAdmin(GuardedModelAdmin):
    list_display = [
        'transaction_code',
        'customer',
        'store',
        'date',
        'amount_formatted',
        'status'
    ]
    list_filter = [
        'customer',
        'store',
        'date',
        'amount',
        'status'
    ]

    def amount_formatted(self, instance):
        return 'IDR {:,}'.format(instance.amount).replace(',', '.')

    amount_formatted.short_description = 'jumlah'
    amount_formatted.admin_order_field = 'amount'

admin.site.register(models.CounterTopUp, CounterTopUpAdmin)
admin.site.register(models.CustomerTopUp, CustomerTopUpAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
