from django.db import models
from datetime import datetime

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
    if self.datetime.strftime("%H") == '08': date = ' AM'
    elif self.datetime.strftime("%H") == '14': date = ' PM'
    elif self.datetime.strftime("%H") == '20': date = ' Nig'
    else: date = '?'
    date = self.datetime.strftime("%Y-%m-%d") + date

    return f'{self.score} at {date}'

### Fixtures

# happiest = Score(score = 0)
# happy    = Score(score = 1)
# neutral  = Score(score = 2)
# sad      = Score(score = 3)
# saddest  = Score(score = 4)
# happiest.save()
# happy.save()
# neutral.save()
# sad.save()
# saddest.save()


# entries = [
#   Entry(score = Score.objects.get(score = 2), datetime = datetime(2022, 3, 4, 8), context = 'First'),
#   Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 3, 4, 14), context = 'Second'),
#   Entry(score = Score.objects.get(score = 0), datetime = datetime(2022, 3, 4, 20), context = ''),
#   Entry(score = Score.objects.get(score = 3), datetime = datetime(2022, 3, 5, 8), context = '...'),
#   Entry(score = Score.objects.get(score = 4), datetime = datetime(2022, 3, 5, 14), context = ''),
#   Entry(score = Score.objects.get(score = 1), datetime = datetime(2022, 3, 5, 20), context = ''),
# ]
# for e in entries: e.save()
