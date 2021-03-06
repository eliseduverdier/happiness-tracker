from django.core.management.base import BaseCommand
from tracker.models import Score, Entry

"""
  Emotions emojis
  ๐ ๐ ๐ ๐ ๐ ๐ ๐คฃ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐คฉ ๐ ๐ โบ๏ธ ๐ ๐ ๐ ๐ ๐ ๐คช ๐ ๐ค ๐ค ๐คญ ๐คซ ๐ค ๐ค ๐คจ ๐ ๐ ๐ถ ๐ ๐ ๐ ๐ฌ
  ๐คฅ ๐ ๐ ๐ช ๐คค ๐ด ๐ท ๐ค ๐ค ๐คข ๐คฎ ๐คง ๐ฅต ๐ฅถ๐ต ๐คฏ ๐ค  ๐ฅณ ๐ ๐ค ๐ง ๐ ๐ ๐ โน๏ธ ๐ฎ ๐ฏ ๐ฒ ๐ณ ๐ฅบ ๐ฆ ๐ง ๐จ ๐ฐ ๐ฅ ๐ข ๐ญ ๐ฑ ๐ ๐ฃ
  ๐ ๐ ๐ฉ ๐ซ ๐ฅฑ ๐ค
"""
class Command(BaseCommand):
    help = 'Add scores'

    def handle(self, *args, **options):
      print('Deleting all objects...')
      Entry.objects.all().delete()
      Score.objects.all().delete()

      print('Adding scores...')
      scores = [
        Score(score =  0), # happiest ๐
        Score(score =  1), # happy ๐
        Score(score =  2), # neutral ๐
        Score(score =  3), # sad ๐
        Score(score =  4), # depressed ๐
        Score(score =  5), # angry ๐ก
        Score(score =  6), # drunk  ๐ฅด
        Score(score =  7), # exited  ๐
        Score(score =  8), # loving  ๐ฅฐ
        Score(score =  9), # funny ๐คช
        Score(score = 10), # tired ๐
        Score(score = 11), # calm ๐
        Score(score = 12), # neutral ๐
        Score(score = 13), # fearful  ๐ฑ
        Score(score = 14), # depressed ๐ญ
        Score(score = 15), # cheerful ๐
        Score(score = 16), # worried ๐
        Score(score = 17), # tired ๐ด
      ]

      for score in scores: score.save()

      print(' โ Done !')
