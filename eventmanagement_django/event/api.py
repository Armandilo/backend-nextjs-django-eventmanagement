from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Event
from .serializers import EventSerializer
from .forms import EventForm

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_events(request):
    events = Event.objects.all()

    user_id = request.GET.get('user_id', '')

    if user_id:
        events = events.filter(created_by=user_id)

    serializer = EventSerializer(events, many=True)

    return JsonResponse({'data' : serializer.data})

def get_event(request, id):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return JsonResponse({'data' : serializer.data})
    except Event.DoesNotExist:
        return JsonResponse({'error' : 'Event not found'}, status=404)
    

@api_view(['PUT'])
def update_event(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return JsonResponse({'error' : 'Event not found'}, status=404)

    form = EventForm(request.data, request.FILES, instance=event)
    if form.is_valid():
        if form.cleaned_data['eventmode'] == 'Physical':
            address_fields = ['streetaddress', 'city', 'state', 'zipcode']  # Add or remove fields as necessary
            for field in address_fields:
                if not form.cleaned_data[field]:
                    return JsonResponse({'error' : f'{field} is required for physical events.'}, status=400)
        event = form.save()
        return JsonResponse({'success' : True})
    return JsonResponse({'error' : form.errors.as_json()}, status=400)

    
@api_view(['POST'])
def create_event(request):
    form = EventForm(request.POST, request.FILES)
    if form.is_valid():
        if form.cleaned_data['eventmode'] == 'Physical':
            address_fields = ['streetaddress', 'city', 'state', 'zipcode']  # Add or remove fields as necessary
            for field in address_fields:
                if not form.cleaned_data[field]:
                    return JsonResponse({'error' : f'{field} is required for physical events.'}, status=400)
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        return JsonResponse({'success' : True})
    return JsonResponse({'error' : form.errors.as_json()}, status=400)

@api_view(['DELETE'])
def delete_event(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return JsonResponse({'error' : 'Event not found'}, status=404)

    event.delete()

    return JsonResponse({'success' : True})