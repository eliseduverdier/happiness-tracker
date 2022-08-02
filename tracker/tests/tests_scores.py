from django.test import TestCase
from tracker.models import Score

class ScoreTestCase(TestCase):
  def setUp(self):
    Score.objects.create(score = 0)
    Score.objects.create(score = 4)
    Score.objects.create(score = 100)

  def test_Entrys(self):
    happy = Score.objects.get(score = 0)
    sad = Score.objects.get(score = 4)
    not_an_emotion = Score.objects.get(score = 100)

    self.assertEqual(happy.__str__(), '😀')
    self.assertEqual(sad.__str__(), '😖️')
    self.assertEqual(not_an_emotion.__str__(), '🟡')
