from django.shortcuts import render

from accounts.models import User
from events.models import Event


# Create your views here.
def home_page(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()

    context = {
        'users': users,
        'events': events
    }
    return render(request, 'home.html', context)
