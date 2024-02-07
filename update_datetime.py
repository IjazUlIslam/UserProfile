from django.core.management.base import BaseCommand
from django.utils import timezone
from UserProfile.models import DateTime
from pytz import utc, timezone
from datetime import datetime
import pytz


def convert_to_utc(var_date_time):
    count = 0
    with open('count_store.txt', 'r') as file: 
        starting_point = int(file.read())
        if starting_point < 100:
            for dt in var_date_time:
                if dt.time_zone == 'PST':
                    pst_dt = dt.date_time.replace(tzinfo=None)
                    pacific_timezone = pytz.timezone('US/Pacific')
                    pst_time = pacific_timezone.localize(pst_dt, is_dst=None)
                    utc_time = pst_time.astimezone(timezone('utc'))
                    dt.date_time = utc_time
                    dt.time_zone = 'UTC'
                    dt.save()
                    count +=1
                    if count == 10:
                        break
                    starting_point +=1
                    if starting_point == 100:
                        with open('count_store.txt', "w") as file:
                            file.write(str(0))
                    else:
                        with open('count_store.txt', "w") as file:
                            file.write(str(starting_point))


def convert_to_pst(var_date_time):
    count = 0
    for dt in var_date_time:
        if dt.time_zone == 'UTC':
            utc_dt = dt.date_time.replace(tzinfo=None)
            utc_timezone = pytz.timezone('UTC')
            utc_time = utc_timezone.localize(utc_dt, is_dst=None)
            pst_time = utc_time.astimezone(timezone('Asia/Kolkata'))
            dt.date_time = pst_time
            dt.time_zone = 'PST'
            dt.save()
            count +=1
            if count == 10:
                    break
                    

class Command(BaseCommand):
    help = 'Update datetime'

    def handle(self, *args, **options):
        # Get all events from the database
        var_date_time = DateTime.objects.all()
        convert_to_utc(var_date_time)

        with open('count_store.txt', 'r') as file: 
            starting_point = int(file.read())
            if starting_point == 100:
                convert_to_pst(var_date_time)
