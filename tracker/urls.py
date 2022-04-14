from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.FilterByDateBetweenView.as_view(), name='index'),
    path('entry/<int:pk>/', views.DetailView.as_view(), name='entry'),
    path('new', views.new, name='new'),
    path('graph', views.graph, name='graph'),
]
