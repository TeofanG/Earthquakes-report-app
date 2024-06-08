# earthquake_app/management/commands/delete_events.py

from django.core.management.base import BaseCommand
from earthquake_app.models import Event

class Command(BaseCommand):
    help = 'Delete all events'

    def handle(self, *args, **options):
        Event.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all events'))
