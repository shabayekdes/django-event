from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import RegisterUserForm
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


@login_required(login_url="/login")
def my_account(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/my_account.html', context)


def login_page(request):
    page = "login"
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {
        "page": page
    }
    return render(request, 'auth/login_register.html', context)


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

    return render(request, 'auth/logout.html')


def register_page(request):
    page = "register"
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        login(request, user)
        return redirect('home')

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'auth/login_register.html', context)