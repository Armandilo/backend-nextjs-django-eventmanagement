from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'company', 'category', 'description', 'start_date', 'price', 'eventmode', 'streetaddress', 'city', 'state', 'zipcode', 'image']
        exclude = ['created_by']