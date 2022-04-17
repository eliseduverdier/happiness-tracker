from django.core.management.base import BaseCommand, CommandError
from tracker.models import Score, Entry
from datetime import datetime
from django.utils import timezone
import pytz

class Command(BaseCommand):
    help = 'Add fixtures'

    def handle(self, *args, **options):
      print('Deleting all objects...')
      Entry.objects.all().delete()
      Score.objects.all().delete()

      print('Adding fixtures...')
      happiest = Score(score = 0)
      happy    = Score(score = 1)
      neutral  = Score(score = 2)
      sad      = Score(score = 3)
      saddest  = Score(score = 4)
      happiest.save()
      happy.save()
      neutral.save()
      sad.save()
      saddest.save()

      timezone.now()
      entries = [
        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 14, 8, tzinfo=pytz.UTC), context = 'First txt...'),
        Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 4, 14, 14, tzinfo=pytz.UTC), context = 'Second txt...'),
        Entry(score = Score.objects.get(score = 0), datetime = datetime(2022, 4, 14, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 4, 15, 8, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 15, 14, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 4, 15, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 16, 12, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 4, 16, 20, tzinfo=pytz.UTC), context = 'txt...'),

        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 17, 9, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 4, 17, 12, tzinfo=pytz.UTC), context = 'txt...'),
        Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 4, 17, 20, tzinfo=pytz.UTC), context = 'txt...'),
      ]
      for e in entries: e.save()
      print(' ✅ Done !')
