from django.forms import ModelForm
from tracker.models import Entry

# Create the form class.
class EntryForm(ModelForm):
  class Meta:
      model = Entry
      fields = ['score', 'datetime', 'context']

# Creating a form to add an Entry.
form = EntryForm()

# Creating a form to change an existing Entry.
entry = Entry.objects.get(pk=1)
form = EntryForm(instance=Entry)
