from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.graph, name='graph'),
    path('list', views.FilterByDateBetweenView.as_view(), name='list'),
    path('analytics', views.AnalyticsView.as_view(), name='analytics'),
    path('new', views.new, name='new'),
    path('entry/<int:pk>/', views.DetailView.as_view(), name='entry'),
    path('edit/<int:pk>/', views.EntryUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.EntryDeleteView.as_view(), name='delete'),
]
