# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='address',
        ),
    ]
