# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounterTopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('method', models.CharField(choices=[('transfer', 'Transfer'), ('manual', 'Manual')], max_length=30)),
            ],
            options={
                'verbose_name': 'Top up counter',
                'verbose_name_plural': 'Top up counter',
                'permissions': (('view_countertopup', 'Can view counter top up'),),
            },
        ),
        migrations.CreateModel(
            name='CustomerTopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Top up pengguna',
                'verbose_name_plural': 'Top up pengguna',
                'permissions': (('view_customertopup', 'Can view customer top up'),),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Pembayaran',
                'verbose_name_plural': 'Pembayaran',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('transaction_code', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('remarks', models.TextField()),
            ],
            options={
                'verbose_name': 'Transaksi toko',
                'verbose_name_plural': 'Transaksi toko',
                'permissions': (('view_transaction', 'Can view transaction'),),
            },
        ),
    ]
