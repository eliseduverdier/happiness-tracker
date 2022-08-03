from django.test import TestCase
from tracker.models import Entry, Score
from datetime import datetime
from django.utils import timezone
import pytz

class EntryTestCase(TestCase):
  def setUp(self):
    timezone.now()
    Score.objects.create(score = 0)
    Entry.objects.create(score = Score.objects.get(score = 0), datetime = datetime(2000, 1, 1, 8, 0, 0, tzinfo=pytz.UTC), context = 'Testing entries'),

  def test_entries(self):
    entry = Entry.objects.first()

    self.assertEqual(entry.__str__(), '😀 at 2000-01-01 AM')
    self.assertEqual(entry.get_days_since_year_beginning(), 1)


class ScoreTestCase(TestCase):
  def setUp(self):
    Score.objects.create(score = 0)
    Score.objects.create(score = 4)
    Score.objects.create(score = 100)

  def test_scores(self):
    happy = Score.objects.get(score = 0)
    sad = Score.objects.get(score = 4)
    not_an_emotion = Score.objects.get(score = 100)

    self.assertEqual(happy.__str__(), '😀')
    self.assertEqual(sad.__str__(), '😖️')
    self.assertEqual(not_an_emotion.__str__(), '🟡')
