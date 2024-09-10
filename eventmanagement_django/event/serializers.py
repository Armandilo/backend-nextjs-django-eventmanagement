from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'company', 'category', 'description', 'start_date', 'price', 'eventmode', 'streetaddress', 'city', 'state', 'zipcode', 'created_by', 'created_at', 'updated_at', 'image', 'image_url')