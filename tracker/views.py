from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Entry, Score

def index(request):
  return render(request, 'tracker/index.html', {
      'entries': Entry.objects.all(),
  })

def entry(request, entry_id):
  return render(request, 'tracker/entry.html', {
      'entry': Entry.objects.get(id = entry_id),
  })

def new(request):
  '''TODO: creating new entry'''
  if request.method =='POST':
    try:
      print('saving data')
      # new_entry = form_data.save()
      # new_entry.save()
    except (KeyError, Entry.DoesNotExist):
      return render(request, 'tracker/entry.html', {
          'entry': entry,
          'error_message': "You didn't select a happiness level or a date.",
      })
    else:
      return HttpResponseRedirect('tracker:index')
  else:
    return render(request, 'tracker/new.html', {
        'scores': Score.objects.all()
    })
