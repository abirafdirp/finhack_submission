import uuid

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BaseTransaction(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True

METHOD = (
    ('transfer', 'Transfer'),
    ('manual', 'Manual')
)


@python_2_unicode_compatible
class CounterTopUp(BaseTransaction):
    counter = models.ForeignKey('users.User', related_name='counter_top_ups')
    method = models.CharField(choices=METHOD, max_length=30)

    class Meta:
        verbose_name = 'Top up counter'
        verbose_name_plural = 'Top up counter'

    def save(self, *args, **kwargs):
        return super(BaseTransaction, self).save(*args, **kwargs)


@python_2_unicode_compatible
class CustomerTopUp(BaseTransaction):
    customer = models.ForeignKey('users.User',
                                 related_name='top_ups')
    # counter will be determined at admin (request.user)
    counter = models.ForeignKey('users.User', blank=True, null=True,
                                related_name='customer_top_ups')

    def save(self, *args, **kwargs):
        # disabled temporarily for testing purposes
        # self.date = timezone.now()
        return super(CustomerTopUp, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Top up pengguna'
        verbose_name_plural = 'Top up pengguna'


@python_2_unicode_compatible
class Payment(BaseTransaction):
    user = models.ForeignKey('users.User')

    class Meta:
        verbose_name = 'Pembayaran'
        verbose_name_plural = 'Pembayaran'

    def save(self, *args, **kwargs):
        return super(Payment, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Transaction(BaseTransaction):
    customer = models.ForeignKey('users.User', related_name='transactions')
    store = models.ForeignKey('store.Store', related_name='transactions')
    transaction_code = models.UUIDField(default=uuid.uuid4,
                                        unique=True,
                                        editable=False,
                                        blank=True,
                                        null=True)

    # remarks from the store, such as detail of the transaction
    remarks = models.TextField()

    def save(self, *args, **kwargs):
        # disabled temporarily for testing purposes
        self.date = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Transaksi toko'
        verbose_name_plural = 'Transaksi toko'
