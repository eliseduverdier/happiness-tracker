from django.db import models

class Score(models.Model):
  score = models.IntegerField(default=0)

class Entry(models.Model):
  score = models.ForeignKey(Score) # on_delete=models.CASCADE
  context = models.CharField(max_length=200)
  datetime = models.DateTimeField('datetime')
