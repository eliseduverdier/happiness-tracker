from .models import *

def load_fixtures():
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

  entries = [
    Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 3, 4, 8), context = 'First txt...'),
    Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 3, 4, 14), context = 'Second txt...'),
    Entry(score = Score.objects.get(score = 0), datetime = datetime(2022, 3, 4, 20), context = 'txt...'),
    Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 3, 5, 8), context = 'txt...'),
    Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 3, 5, 14), context = 'txt...'),
    Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 3, 5, 20), context = 'txt...'),
  ]
  for e in entries: e.save()
