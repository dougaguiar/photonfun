from django.apps import AppConfig


class ScorekeeperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scorekeeper'

    def ready(self):
        import scorekeeper.signals