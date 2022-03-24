from django.db import models
from datetime import datetime, date

class Score(models.Model):
  score = models.IntegerField(default=0)
  def __str__(self):
    if self.score == 0: return '😀️'
    if self.score == 1: return '🙂️'
    if self.score == 2: return '😐️'
    if self.score == 3: return '🙁️'
    if self.score == 4: return '😖️'

class Entry(models.Model):
  score = models.ForeignKey(Score, on_delete=models.PROTECT)
  datetime = models.DateTimeField('datetime')
  context = models.CharField(max_length=200)

  def __str__(self):
    date = self.datetime.strftime("%Y-%m-%d") + self.get_time_of_day()
    return f'{self.score} at {date}'

  def get_time_of_day(self):
    hour = int(self.datetime.strftime("%H"))
    if hour < 12: return ' AM'
    elif hour < 18: return ' PM'
    elif hour < 24: return ' N'
    else: return '?'

  def days_since_year_beginning(self):
    return self.datetime.toordinal() - date(self.datetime.year, 1, 1).toordinal() + 1

### Fixtures: decomment to populate database
# from .fixtures import *
# load_fixtures()
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
