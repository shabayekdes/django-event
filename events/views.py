from django.shortcuts import render, redirect

from events.models import Event


def show_event(request, pk):
    event = Event.objects.get(id=pk)
    context = {
        'event': event,
        'participants': event.participants.all
    }
    return render(request, 'events/show_event.html', context)


def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.participants.add(request.user)
        return redirect('show_event', pk=event.id)

    context = {
        'event': event
    }
    return render(request, 'events/event_confirmation.html', context)
