from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('earthquake_app:add_event')
    else:
        form = EventForm()

    return render(request, 'earthquake_app/add_event.html', {'form': form})

def show_events(request):
    # Implement filtering based on magnitude and depth
    magnitude_filter = request.GET.get('magnitude')
    depth_filter = request.GET.get('depth')

    filtered_events = Event.objects.all()
    if magnitude_filter:
        filtered_events = filtered_events.filter(magnitude=magnitude_filter)
    if depth_filter:
        filtered_events = filtered_events.filter(depth=depth_filter)

    return render(request, 'earthquake_app/show_events.html', {'events': filtered_events})
