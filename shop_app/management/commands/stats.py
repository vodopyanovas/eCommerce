from django.core.management.base import BaseCommand, CommandError
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Shows products statistics'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass
