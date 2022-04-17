from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Entry, Score
from .forms.forms import EntryForm
from .serializers import EntrySerializer

class DetailView(generic.DetailView):
  model = Entry
  template_name = 'tracker/entry.html'

class FilterByDateBetweenView(generic.ListView):
  template_name = 'tracker/list.html'
  context_object_name = 'entries'

  def get_queryset(self):
    start = self.request.GET.get('start', None)
    end = self.request.GET.get('end', None)
    if start and end:
      return Entry.objects.filter(datetime__range=(start+' 00:00:00', end+' 23:59:59' )).order_by('-datetime').all()
    else:
      return Entry.objects.order_by('-datetime').all()

def graph(request):
  serializer = EntrySerializer(Entry.objects.order_by('datetime').all(), many=True)
  return render(request, 'tracker/graph.html', {
    'entries':  serializer.data
  })

def new(request):
  if request.method =='POST':
    try:
      entry = EntryForm(request.POST)
      if entry.is_valid():
        entry.save()
        return HttpResponseRedirect('/tracker/')
      else:
        print('>>>>>>>>>>>>> fail')
        raise Exception('Invalid entry?')
    except (Exception):
      return render(request, 'tracker/new.html', {
        'scores': Score.objects.all(),
        'error_message': "You didn’t select a happiness level or a date.",
      })
  else:
    return render(request, 'tracker/new.html', {
        'scores': Score.objects.all()
    })
