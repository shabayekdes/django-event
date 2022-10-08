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


def user_details(request, pk):
    user = User.objects.get(id=pk)

    context = {
        'user': user
    }
    return render(request, 'users/show_details.html', context)


def my_account(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/my_account.html', context)
