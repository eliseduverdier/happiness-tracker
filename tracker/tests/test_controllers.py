from django.test import Client, TestCase, tag
from tracker.models import Entry, Score
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz

class ControllerTestCase(TestCase):
  def setUp(self):
    timezone.now()
    Score.objects.create(score = 0)
    Entry.objects.create(score = Score.objects.get(score = 0), datetime = datetime(2000, 1, 1, 8, 0, 0, tzinfo=pytz.UTC), context = 'Testing entries')
    self.user = User.objects.create_user(username='testuser', password='123456')

  def test_list(self):
    c = Client()
    response = c.get('/list')
    self.assertEqual(200, response.status_code)
    self.assertIn('Testing entries', response.content.decode())
    self.assertIn('😀', response.content.decode())

  def test_analytics(self):
    c = Client()
    response = c.get('/analytics')

    self.assertEqual(200, response.status_code)
    self.assertIn('count', response.content.decode())
    self.assertIn('1', response.content.decode())

  def test_new(self):
    c = Client()
    response = c.get('/new')
    self.assertEqual(302, response.status_code)
    self.assertEqual('/', response.headers['Location'])

    c.force_login(self.user)
    response = c.get('/new')

    self.assertEqual(200, response.status_code)
    self.assertIn('😀', response.content.decode())
    self.assertIn('textarea', response.content.decode())

  def test_create(self):
    c = Client()
    c.force_login(self.user)
    response = c.post('/new', {'score': '2', 'datetime': '2000-01-02T08:00', 'context': 'Adding an entry'})
    self.assertEqual(302, response.status_code)

    response = c.get('/list')
    self.assertIn('Adding an entry', response.content.decode())
    self.assertIn('2000-01-02 08:00', response.content.decode())

  def test_edit(self):
    c = Client()
    c.force_login(self.user)
    response = c.post('/edit/1/', {'datetime': '2000-01-02T08:00', 'context': 'Edited an entry'})
    self.assertEqual(302, response.status_code)

    response = c.get('/list')
    self.assertIn('Edited an entry', response.content.decode())

  def test_delete(self):
    c = Client()
    c.force_login(self.user)
    response = c.get('/delete/1/')
    self.assertIn('Are you sure you want to delete "😀 at 2000-01-01 AM"?', response.content.decode())

    response = c.post('/delete/1/', {})
    self.assertEqual(302, response.status_code)

    response = c.get('/list')
    self.assertNotIn('Testing entries', response.content.decode())

