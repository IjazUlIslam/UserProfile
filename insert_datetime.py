from UserProfile.models import DateTime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate random datetime'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of datetime to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            obj = DateTime(
                date_time='2024-01-01T01:00:00',
                time_zone='PST'
            )
            obj.save()
