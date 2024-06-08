from django.urls import path
from . import views
app_name = 'earthquake_app'

urlpatterns = [
    path('add', views.add_event, name='add_event'),
    path('events', views.show_events, name='show_events'),
]
