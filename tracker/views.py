from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Entry, Score
from .forms.forms import EntryForm
from .serializers import EntrySerializer, AnalyticsSerializer
from django.db.models import Count

class DetailView(generic.DetailView):
  model = Entry
  template_name = 'entry.html'


class EntryDeleteView(generic.DeleteView):
  model = Entry
  success_url = '/list'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return HttpResponseRedirect('/list')

    return super().dispatch(request, *args, **kwargs)


class EntryUpdateView(generic.UpdateView):
  model = Entry
  success_url = '/list'
  fields = ['datetime', 'context']
  template_name_suffix = '_update_form'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return HttpResponseRedirect('/list')

    return super().dispatch(request, *args, **kwargs)


class FilterByDateBetweenView(generic.ListView):
  template_name = 'list.html'
  context_object_name = 'entries'

  def get_queryset(self):
    start = self.request.GET.get('start', None)
    end = self.request.GET.get('end', None)
    if start and end:
      return Entry.objects.filter(datetime__range=(start+' 00:00:00', end+' 23:59:59' )).order_by('-datetime').all()
    else:
      return Entry.objects.order_by('-datetime').all()

class AnalyticsView(generic.ListView):
  template_name = 'analytics.html'
  context_object_name = 'entries'

  def get_queryset(self):
    entries_by_count = Entry.objects.values('score').annotate(count=Count('score')).order_by('-count').all()
    entries = {}
    for score in entries_by_count:
      score_object = Score.objects.get(pk = score['score'])
      entries_for_score = Entry.objects.filter(score=score_object).all()
      serializer = EntrySerializer(entries_for_score, many=True)
      entries[score_object.__str__()] = serializer.data
    return entries

# class AnalyticsView(generic.ListView):
#   template_name = 'analytics.html'
#   context_object_name = 'entries'

#   def get_queryset(self):
#     serialized = AnalyticsSerializer(entries, many=True)
#     return serialized.data


def graph(request):
  serializer = EntrySerializer(Entry.objects.order_by('-datetime').all(), many=True)
  return render(request, 'graph.html', {
    'entries':  serializer.data
  })


def new(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/')

  if request.method =='POST':
    try:
      entry = EntryForm(request.POST)
      if entry.is_valid():
        entry.save()
        return HttpResponseRedirect('/')
      else:
        raise Exception('Invalid entry?')
    except (Exception):
      return render(request, 'new.html', {
        'scores': Score.objects.all(),
        'error_message': "You didn’t select a happiness level or a date.",
      })
  else:
    return render(request, 'new.html', {
        'scores': Score.objects.all()
    })
