from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'finhack_bca.users'
    verbose_name = 'Pengguna'

    def ready(self):
        import finhack_bca.users.signals
