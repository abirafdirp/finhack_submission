from django.db import models
from django.utils import timezone


class BaseTransaction(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CounterTopUp(BaseTransaction):
    counter = models.ForeignKey('users.User')

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(CounterTopUp, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(Payment, self).save(*args, **kwargs)


class Transaction(BaseTransaction):
    customer = models.ForeignKey('users.User')
    store = models.ForeignKey('store.Store')

    # remarks from the store, such as detail of the transaction
    remarks = models.TextField()

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)
