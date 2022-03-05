from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('entry/<int:entry_id>/', views.entry, name='entry'),

]
