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

print('This might take a while...')
print('Generating Stores, Counters, Customers, Top Ups, Payments,'
      'and Transactions')


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
date_of_births = [
    '1970-03-01',
    '1979-04-02',
    '1973-05-01',
    '1985-06-03',
    '2000-07-04',
    '1990-08-09',
    '1980-09-11',
]


# register counters
for a in range(0, 10):
    User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='qwerty',
        type='counter',
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        address=fake.address(),
        city=fake.city(),
        mobile_number=fake.phone_number(),
        date_of_birth=random.choice(date_of_births)
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
for c in range(0, 10):
    User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='qwerty',
        type='customer',
        mobile_number=fake.phone_number(),
        date_of_birth=random.choice(date_of_births)
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


# generate stores and theirs accounts
for x in range(0, 8):
    store = Store.objects.create(
        name=fake.company(),
        domain=fake.url(),
        short_description=fake.text(max_nb_chars=200)
    )
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='qwerty',
        type='store',
        mobile_number=fake.phone_number(),
        date_of_birth=random.choice(date_of_births)
    )
    user.stores.add(store)


stores = Store.objects.all()

transaction_amounts = [10000, 50000, 30000, 300000, 500000, 78000,
                      40000, 33333, 29000, 157000]


fake_datetime2 = datetime.datetime(2016, 1, 1)
fake_datetime_timezoned2 = timezone_it(fake_datetime)

users = User.objects.all()
# simulate transactions
for user in users:
    if user.is_staff:
        continue
    fake_datetime_transaction = fake_datetime_timezoned2
    for store in stores:
        transaction_amount = random.choice(transaction_amounts)
        if user.balance < transaction_amount:
            break
        Transaction.objects.create(
            date=fake_datetime_transaction,
            store=store,
            customer=user,
            amount=transaction_amount,
            remarks=fake.text(max_nb_chars=100),
            status=random.choice([True, True, True, True, False])
        )
        fake_datetime_transaction += add_random_days(long=False)

