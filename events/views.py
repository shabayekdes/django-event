from django.shortcuts import render

from events.models import Event


def show_event(request, pk):
    event = Event.objects.get(id=pk)
    context = {
        'event': event
    }
    return render(request, 'events/show_event.html', context)
