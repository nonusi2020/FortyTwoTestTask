from django.core.management.base import BaseCommand
from django.apps import apps
import sys


class Command(BaseCommand):
    help = 'data on project models and the count of objects in every model.'

    def handle(self, *args, **options):
        sys.stdout.write('Model name - Count of objects')
        for model in apps.get_models():
            msg = '{} - {} \n'.format(model.__name__, model.objects.count())
            sys.stdout.write(msg)
            sys.stderr.write('Error: ' + msg)
