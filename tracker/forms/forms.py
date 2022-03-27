from django.forms import ModelForm
from tracker.models import Entry

# Create the form class.
class EntryForm(ModelForm):
  class Meta:
      model = Entry
      fields = ['score', 'datetime', 'context']
  def clean_rowname(self):
      return self.cleaned_data['context'] or None
