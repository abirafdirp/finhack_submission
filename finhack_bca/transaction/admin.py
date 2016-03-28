from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

    def get_queryset(self, request):
        return models.CustomerTopUp.objects.filter(customer=request.user)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return models.CustomerTopUp._meta.get_all_field_names()
        return self.readonly_fields

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:transaction_customertopup_changelist'))

        return super(CustomerTopUpAdmin, self).change_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:transaction_customertopup_changelist'))

        return super(CustomerTopUpAdmin, self).delete_view(request, object_id, extra_context)

    def history_view(self, request, object_id, extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:transaction_customertopup_changelist'))

        return super(CustomerTopUpAdmin, self).history_view(request, object_id, extra_context)


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
    search_fields = [
        'transaction_code',
        'customer',
        'store'
    ]

    def amount_formatted(self, instance):
        return 'IDR {:,}'.format(instance.amount).replace(',', '.')

    amount_formatted.short_description = 'jumlah'
    amount_formatted.admin_order_field = 'amount'

admin.site.register(models.CounterTopUp, CounterTopUpAdmin)
admin.site.register(models.CustomerTopUp, CustomerTopUpAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
