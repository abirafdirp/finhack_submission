import os
import datetime
import random
from dateutil.relativedelta import relativedelta

import pytz

from faker import Faker

import django
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'config.settings.local')
django.setup()

from finhack_bca.transaction.models import CustomerTopUp
from finhack_bca.transaction.models import CounterTopUp
from finhack_bca.transaction.models import Payment
from finhack_bca.transaction.models import Transaction
from finhack_bca.store.models import Store
from finhack_bca.users.models import User


def timezone_it(datetime):
    return pytz.timezone('Asia/Jakarta').localize(datetime)


def add_random_days(long=True):
    if long:
        days = relativedelta(days=random.randint(20, 30),
                             hours=random.randint(1, 23),
                             minutes=random.randint(1, 59))
    else:
        days = relativedelta(days=random.randint(1, 15),
                             hours=random.randint(1, 23),
                             minutes=random.randint(1, 59))
    return days

CustomerTopUp.objects.all().delete()
CounterTopUp.objects.all().delete()
Payment.objects.all().delete()
Transaction.objects.all().delete()
Store.objects.all().delete()
users = User.objects.all()

for user in users:
    if not user.is_superuser:
        user.delete()

fake = Faker()
fake.name()


# register counters
for a in range(0, 15):
    User.objects.create(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        type='counter',
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        address=fake.address(),
        city=fake.city()
    )

# simulate counter top ups
balances = [800000, 700000, 500000, 1000000, 2000000, 50000, 250000]
counters = User.objects.filter(type='counter')

fake_datetime = datetime.datetime(2015, 10, 1)
fake_datetime_timezoned = timezone_it(fake_datetime)

methods = ['transfer', 'manual']

for counter in counters:
    fake_datetime_topup = fake_datetime_timezoned
    topups = random.randint(1, 5)
    for topup in range(0, topups):
        CounterTopUp.objects.create(
            counter=counter,
            date=fake_datetime_topup,
            amount=random.choice(balances),
            status=True,
            method=random.choice(methods)
        )
        fake_datetime_topup += add_random_days()


# register customers
for c in range(0, 40):
    User.objects.create(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        type='customer',
    )

# simulate customer top ups
topup_amounts = [100000, 200000, 50000, 30000, 10000, 15000, 50000]
customers = User.objects.filter(type='customer')

for customer in customers:
    fake_datetime_topup = fake_datetime_timezoned
    topups = random.randint(1, 10)
    for custtopup in range(0, topups):
        topup_amount = random.choice(topup_amounts)
        counter = random.choice(list(counters))
        if counter.balance < topup_amount:
            while counter.balance < topup_amount:
                counter = random.choice(list(counters))

        CustomerTopUp.objects.create(
            counter=counter,
            customer=customer,
            date=fake_datetime_topup,
            amount=topup_amount,
            status=True
        )
        fake_datetime_topup += add_random_days(long=False)


# generate stores

for x in range(0, 20):
    Store.objects.create(

    )