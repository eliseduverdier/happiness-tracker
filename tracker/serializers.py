from rest_framework import serializers

class EntrySerializer(serializers.BaseSerializer):
  def to_representation(self, instance):
    return {
        'score': instance.score.__str__(),
        'relative_days': instance.get_days_since_first_date(),
        'date': instance.datetime.strftime("%d/%m"),
        'time': instance.get_time_of_day(),
        'context': '' if not instance.context else instance.context
    }
