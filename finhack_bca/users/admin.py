# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    fieldsets = AuthUserAdmin.fieldsets + (
            (None, {'fields': ('type',)}),
    )

    list_display = [
        'username',
        'email',
        'type',
        'balance_formatted',
        'city',
        'address'
    ]
    list_filter = [
        'type'
    ]

    def balance_formatted(self, instance):
        return 'IDR {:,}'.format(instance.balance).replace(',', '.')

    balance_formatted.short_description = 'saldo'
    balance_formatted.admin_order_field = 'balance'
