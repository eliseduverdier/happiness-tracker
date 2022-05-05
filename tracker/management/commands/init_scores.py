from django.core.management.base import BaseCommand
from tracker.models import Score, Entry

class Command(BaseCommand):
    help = 'Add scores'

    def handle(self, *args, **options):
      print('Deleting all objects...')
      Entry.objects.all().delete()
      Score.objects.all().delete()

      print('Adding scores...')
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

      print(' ✅ Done !')
