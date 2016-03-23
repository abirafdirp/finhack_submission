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
        # disabled temporarily for testing purposes
        # self.date = timezone.now()
        return super(BaseTransaction, self).save(*args, **kwargs)

METHOD = (
    ('transfer', 'Transfer'),
    ('manual', 'Manual')
)


class CounterTopUp(BaseTransaction):
    counter = models.ForeignKey('users.User')
    method = models.CharField(choices=METHOD, max_length=30)

    class Meta:
        verbose_name = 'Top up counter'
        verbose_name_plural = 'Top up counter'

    def save(self, *args, **kwargs):
        super(BaseTransaction, self).save(*args, **kwargs)
        if self.status:
            self.counter.balance += self.amount
            self.counter.save()


class CustomerTopUp(BaseTransaction):
    customer = models.ForeignKey('users.User',
                                 related_name='customer_payments')
    # counter will be determined at admin (request.user)
    counter = models.ForeignKey('users.User', blank=True, null=True,
                                related_name='customer_top_ups')

    def save(self, *args, **kwargs):
        # disabled temporarily for testing purposes
        # self.date = timezone.now()
        super(CustomerTopUp, self).save(*args, **kwargs)
        if self.status:
            self.counter.balance -= self.amount
            self.customer.balance += self.amount
            self.counter.save()
            self.customer.save()

    class Meta:
        verbose_name = 'Top up pengguna'
        verbose_name_plural = 'Top up pengguna'


class Payment(BaseTransaction):
    user = models.ForeignKey('users.User')

    class Meta:
        verbose_name = 'Pembayaran'
        verbose_name_plural = 'Pembayaran'


class Transaction(BaseTransaction):
    customer = models.ForeignKey('users.User')
    store = models.ForeignKey('store.Store')
    transaction_code = models.UUIDField(default=uuid.uuid4,
                                        unique=True,
                                        editable=False)

    # remarks from the store, such as detail of the transaction
    remarks = models.TextField()

    def save(self, *args, **kwargs):
        # disabled temporarily for testing purposes
        # self.date = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Transaksi toko'
        verbose_name_plural = 'Transaksi toko'
