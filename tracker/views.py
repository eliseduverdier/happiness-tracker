from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Entry, Score
from .forms import EntryForm


class IndexView(generic.ListView):
  template_name = 'tracker/index.html'
  context_object_name = 'entries'

  def get_queryset(self):
      return Entry.objects.all( )


class DetailView(generic.DetailView):
    model = Entry
    template_name = 'tracker/entry.html'

def new(request):
  if request.method =='POST':
    try:
      entry = EntryForm(request.POST)
      if entry.is_valid():
        entry.save()
      return HttpResponseRedirect('/tracker/')
    except (KeyError, Entry.DoesNotExist):
      return render(request, 'tracker/new.html', {
        'scores': Score.objects.all(),
        'error_message': "You didn’t select a happiness level or a date.",
      })
  else:
    return render(request, 'tracker/new.html', {
        'scores': Score.objects.all()
    })
