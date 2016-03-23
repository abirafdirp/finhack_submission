import uuid

from django.db import models
from django.utils import timezone


class BaseTransaction(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(BaseTransaction, self).save(*args, **kwargs)


class CounterTopUp(BaseTransaction):
    counter = models.ForeignKey('users.User')


class CustomerTopUp(BaseTransaction):
    customer = models.ForeignKey('users.User',
                                 related_name='customer_payments')
    # counter will be determined at admin (request.user)
    counter = models.ForeignKey('users.User', blank=True, null=True,
                                related_name='customer_top_ups')

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(CustomerTopUp, self).save(*args, **kwargs)


class Payment(BaseTransaction):
    user = models.ForeignKey('users.User')


class Transaction(BaseTransaction):
    customer = models.ForeignKey('users.User')
    store = models.ForeignKey('store.Store')
    transaction_code = models.UUIDField(default=uuid.uuid4,
                                        unique=True,
                                        editable=False)

    # remarks from the store, such as detail of the transaction
    remarks = models.TextField()

    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)
