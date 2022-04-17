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
  context = models.CharField(max_length=200, null=True, blank = True)

  def __str__(self):
    date = self.datetime.strftime("%Y-%m-%d") +' '+  self.get_time_of_day()
    return f'{self.score} at {date}'

  def get_time_of_day(self):
    hour = int(self.datetime.strftime("%H"))
    if hour < 12: return 'AM'
    elif hour < 18: return 'PM'
    elif hour < 24: return 'N'
    else: return '?'

  def get_days_since_year_beginning(self):
    return self.datetime.toordinal() - date(self.datetime.year, 1, 1).toordinal() + 1

  def get_days_since_first_date(self):
    return int(self.datetime.toordinal() - Entry.objects.order_by('datetime').first().datetime.toordinal())
