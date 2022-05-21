from rest_framework import serializers
from django.utils import timezone

class EntrySerializer(serializers.BaseSerializer):
  def to_representation(self, instance):
    return {
        'score': instance.score.__str__(),
        'relative_days': instance.get_days_since_first_date(),
        'relative_days_since_last': instance.get_days_since_last_date(),
        'date': instance.datetime.strftime("%d/%m"),
        'datejs': instance.datetime.strftime("%Y-%m-%d"),
        'time': instance.get_time_of_day(),
        'hour': timezone.localtime(instance.datetime).strftime("%H"),
        'context': '' if not instance.context else instance.context
    }
