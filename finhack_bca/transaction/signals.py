from django.db.models.signals import post_save

from finhack_bca.transaction.models import Payment, Transaction, CustomerTopUp, CounterTopUp


def customer_top_up(sender, instance, created, **kwargs):
    if instance.status:
        Payment.objects.create(
            date=instance.date,
            amount=instance.amount,
            status=True,
            user=instance.counter
        )
        instance.customer.balance += instance.amount
        instance.customer.save()


def counter_top_up(sender, instance, created, **kwargs):
    if instance.status:
        instance.counter.balance += instance.amount
        instance.counter.save()
        

def payment(sender, instance, created, **kwargs):
    instance.user.balance -= instance.amount
    instance.user.save()


def transaction(sender, instance, created, **kwargs):
    if instance.status:
        instance.store.balance += instance.amount
        instance.store.save()
        Payment.objects.create(
            date=instance.date,
            amount=instance.amount,
            status=True,
            user=instance.customer
        )

post_save.connect(customer_top_up, sender=CustomerTopUp)
post_save.connect(counter_top_up, sender=CounterTopUp)
post_save.connect(transaction, sender=Transaction)
post_save.connect(payment, sender=Payment)

