from django.apps import AppConfig


class FortytwotasksConfig(AppConfig):
    name = 'apps.fortytwoapps'

    def ready(self):
        import apps.fortytwoapps.signals # noqa
