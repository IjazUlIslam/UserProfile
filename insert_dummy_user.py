from UserProfile.models import CustomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            b = CustomUser(
                email=f'dummy{i}@gmail.com',
                first_name='dummy',
                middle_name='',
                last_name='dummy',
                phone_number='+1234567890',
                password='admin'
            )
            b.save()
