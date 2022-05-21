from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.graph, name='graph'),
    path('list', views.FilterByDateBetweenView.as_view(), name='list'),
    path('new', views.new, name='new'),
    path('wheel', views.wheel, name='wheel'),
    path('entry/<int:pk>/', views.DetailView.as_view(), name='entry'),
    path('delete/<int:pk>/', views.EntryDeleteView.as_view(), name='delete'),
]
