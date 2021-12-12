from django.apps import AppConfig


class SumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sume'

    def ready(self) -> None:
        from sume import signals