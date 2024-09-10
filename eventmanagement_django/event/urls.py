from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_events, name='events_list'),
    path('<uuid:id>/', api.get_event, name='event_detail'),
    path('create/', api.create_event, name='api_create_event'),
    path('<uuid:id>/update/', api.update_event, name='api_update_event'),
    path('<uuid:id>/delete/', api.delete_event, name='api_delete_event'),

]