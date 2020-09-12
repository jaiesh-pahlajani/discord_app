from django.core.management import BaseCommand
from modules.dolores import start_dolores


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start_dolores()
