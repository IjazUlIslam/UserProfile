from django.core.management.base import BaseCommand
from UserProfile.models import DateTime
from pytz import timezone
import pytz


def convert_to_utc(dt):
    pst_dt = dt.date_time.replace(tzinfo=None)
    pacific_timezone = pytz.timezone('US/Pacific')
    pst_time = pacific_timezone.localize(pst_dt, is_dst=None)
    utc_time = pst_time.astimezone(timezone('utc'))
    dt.date_time = utc_time
    dt.time_zone = 'UTC'
    dt.save()


def convert_to_pst(dt):
    utc_dt = dt.date_time
    pst_timezone = pytz.timezone('US/Pacific')
    pst_time = utc_dt.astimezone(pst_timezone)
    dt.date_time = pst_time.replace(tzinfo=None)
    dt.time_zone = 'PST'
    dt.save()


class Command(BaseCommand):
    help = 'Update datetime'

    def handle(self, *args, **options):
        # Get all events from the database
        with open('/home/ijaxxijaa/Documents/Django bonus Task1/BonusTask1/count_store.txt', 'r') as file:
            count = int(file.read())
        var_date_time = DateTime.objects.filter(id__gt=count)[:10]
        for dt in var_date_time:
            if dt.time_zone == 'PST':
                convert_to_utc(dt)
            else:
                convert_to_pst(dt)
        with open('/home/ijaxxijaa/Documents/Django bonus Task1/BonusTask1/count_store.txt', "w") as file:
            if not var_date_time:
                first_object = DateTime.objects.first()
                file.write(str(first_object.id))
            else:
                file.write(str(dt.id))
