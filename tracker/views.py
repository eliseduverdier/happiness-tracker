from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Entry, Score
from .forms.forms import EntryForm
from .serializers import EntrySerializer
from django.contrib.auth import authenticate, login
# from django.views.generic.edit import FormView

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
        'error_message': "You didn???t select a happiness level or a date.",
      })
  else:
    return render(request, 'new.html', {
        'scores': Score.objects.all()
    })
