from django.apps import AppConfig


class TransactionConfig(AppConfig):
    name = 'finhack_bca.transaction'
    verbose_name = 'Transaksi'

    def ready(self):
        import finhack_bca.transaction.signals
