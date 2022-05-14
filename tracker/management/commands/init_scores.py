from django.core.management.base import BaseCommand
from tracker.models import Score, Entry

"""
  Emotions emojis
  😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 😉 😊 😇 🥰 😍 🤩 😘 😗 ☺️ 😚 😙 😋 😛 😜 🤪 😝 🤑 🤗 🤭 🤫 🤔 🤐 🤨 😐 😑 😶 😏 😒 🙄 😬
  🤥 😌 😔 😪 🤤 😴 😷 🤒 🤕 🤢 🤮 🤧 🥵 🥶😵 🤯 🤠 🥳 😎 🤓 🧐 😕 😟 🙁 ☹️ 😮 😯 😲 😳 🥺 😦 😧 😨 😰 😥 😢 😭 😱 😖 😣
  😞 😓 😩 😫 🥱 😤
"""
class Command(BaseCommand):
    help = 'Add scores'

    def handle(self, *args, **options):
      print('Deleting all objects...')
      Entry.objects.all().delete()
      Score.objects.all().delete()

      print('Adding scores...')
      scores = [
        Score(score =  0), # happiest 😀
        Score(score =  1), # happy 🙂
        Score(score =  2), # neutral 😐
        Score(score =  3), # sad 🙁
        Score(score =  4), # depressed 😖
        Score(score =  5), # angry 😡
        Score(score =  6), # drunk  🥴
        Score(score =  7), # exited  😄
        Score(score =  8), # loving  🥰
        Score(score =  9), # funny 🤪
        Score(score = 10), # tired 😑
        Score(score = 11), # calm 😌
        Score(score = 12), # neutral 😐
        Score(score = 13), # fearful  😱
        Score(score = 14), # depressed 😭
        Score(score = 15), # cheerful 😊
        Score(score = 16), # worried 😟
        Score(score = 17), # tired 😴
      ]

      for score in scores: score.save()

      print(' ✅ Done !')
