from django.core.management.base import BaseCommand
from tracker.models import Score, Entry
from datetime import datetime
from django.utils import timezone
import pytz

class Command(BaseCommand):
    help = 'Add fixtures'

    def handle(self, *args, **options):
      print('Deleting all objects...')
      Entry.objects.all().delete()

      print('Adding fixtures...')

      timezone.now()
      entries = [
        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 24, 8, tzinfo=pytz.UTC), context = 'First txt...'),
        Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 4, 24, 14, tzinfo=pytz.UTC), context = 'Second txt...'),
        Entry(score = Score.objects.get(score = 0), datetime = datetime(2022, 4, 24, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 4, 25, 8, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 25, 14, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 4, 25, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 26, 12, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 4, 26, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 27, 9, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 27, 12, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 27, 20, tzinfo=pytz.UTC), context = 'txt...'),
      ]
      for e in entries: e.save()
      print(' ✅ Done !')
