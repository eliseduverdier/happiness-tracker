from django.db import models
from datetime import date
from django.utils import timezone

class Score(models.Model):
  score = models.IntegerField(default=0)
  def __str__(self):
    if self.score ==  0: return '😀'
    if self.score ==  1: return '🙂️'
    if self.score ==  2: return '😐️'
    if self.score ==  3: return '🙁️'
    if self.score ==  4: return '😖️'
    if self.score ==  5: return '😡'
    if self.score ==  6: return '🥴'
    if self.score ==  7: return '😄'
    if self.score ==  8: return '🥰'
    if self.score ==  9: return '🤪'
    if self.score == 10: return '😑'
    if self.score == 11: return '😌'
    if self.score == 12: return '😐'
    if self.score == 13: return '😱'
    if self.score == 14: return '😭'
    if self.score == 15: return '😊'
    if self.score == 16: return '😟'
    if self.score == 17: return '😴'
    return '🟡'

class Entry(models.Model):
  score = models.ForeignKey(Score, on_delete=models.PROTECT)
  datetime = models.DateTimeField('datetime')
  context = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    date = timezone.localtime(self.datetime).strftime("%Y-%m-%d") +' '+  self.get_time_of_day()
    return f'{self.score} at {date}'

  def date(self):
    return timezone.localtime(self.datetime).strftime("%Y-%m-%d")

  def time(self):
    return timezone.localtime(self.datetime).strftime("%H:%M")

  def dateinput(self):
    return timezone.localtime(self.datetime).strftime("%Y-%m-%d %H:%M")

  def get_time_of_day(self):
    hour = int(timezone.localtime(self.datetime).strftime("%H"))
    if hour < 12: return 'AM'
    elif hour < 18: return 'PM'
    elif hour < 24: return 'N'
    else: return '?'

  def get_days_since_year_beginning(self):
    return timezone.localtime(self.datetime).toordinal() - date(timezone.localtime(self.datetime).year, 1, 1).toordinal() + 1

  def get_days_since_first_date(self):
    return int(timezone.localtime(self.datetime).toordinal() - Entry.objects.order_by('datetime').first().datetime.toordinal())

  def get_days_since_last_date(self):
    return int(Entry.objects.order_by('datetime').last().datetime.toordinal() - timezone.localtime(self.datetime).toordinal())
