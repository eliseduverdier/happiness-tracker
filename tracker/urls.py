from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('list', views.FilterByDateBetweenView.as_view(), name='list'),
    path('entry/<int:pk>/', views.DetailView.as_view(), name='entry'),
    path('new', views.new, name='new'),
    path('', views.graph, name='graph'),
]
