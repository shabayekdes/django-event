from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from events.forms import SubmissionForm
from events.models import Event, Submission


def show_event(request, pk):
    event = Event.objects.get(id=pk)
    registered = False
    submitted = False
    if request.user.is_authenticated:
        registered = request.user.events.filter(id=event.id).exists()
        submitted = Submission.objects.filter(participant=request.user, event=event.id).exists()

    context = {
        'event': event,
        'participants': event.participants.all,
        'registered': registered,
        'submitted': submitted
    }
    return render(request, 'events/show_event.html', context)


@login_required(login_url="/login")
def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.participants.add(request.user)
        return redirect('show_event', pk=event.id)

    context = {
        'event': event
    }
    return render(request, 'events/event_confirmation.html', context)

@login_required(login_url="/login")
def submission_project(request, pk):
    event = Event.objects.get(id=pk)
    form = SubmissionForm(request.POST or None)
    if form.is_valid():
        submission = form.save(commit=False)
        submission.participant = request.user
        submission.event = event
        submission.save()
        return redirect('my_account')

    context = {
        'event': event,
        'form': form
    }
    return render(request, 'events/submission_project.html', context)

@login_required(login_url="/login")
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)
    event = submission.event
    form = SubmissionForm(request.POST or None, instance=submission)

    if form.is_valid():
        form = form.save(commit=False)
        submission.participant = request.user
        submission.event = event
        submission.save()
        return redirect('my_account')
    context = {
        'event': event,
        'form': form
    }
    return render(request, 'events/submission_project.html', context)
