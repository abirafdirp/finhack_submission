from django.contrib import admin

from finhack_bca.store import models


class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'balance'
    ]


admin.site.register(models.Store, StoreAdmin)