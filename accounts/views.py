from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import RegisterUserForm, UpdateAccountForm
from accounts.models import User
from events.models import Event, Submission


# Create your views here.
def home_page(request):
    users = User.objects.filter(hackathon_participant=True)
    users_count = users.count()
    users = users[0:9]
    events = Event.objects.all()

    context = {
        'users': users,
        'users_count': users_count,
        'events': events,
        'events_range': range(events.count())
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
    submissions = Submission.objects.filter(participant=user)
    context = {
        'user': user,
        'submissions': submissions
    }
    return render(request, 'auth/my_account.html', context)

@login_required(login_url="/login")
def update_account(request):
    form = UpdateAccountForm(instance=request.user)
    if request.method == "POST":
        form = UpdateAccountForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have update account successfully.')
            return redirect('my_account')

    context = {
        'form': form
    }
    return render(request, 'auth/update_account.html', context)


def login_page(request):
    page = "login"
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password was wrong!!')
            return redirect('login')

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


def change_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            user = request.user
            user.set_password(password)
            messages.success(request, 'You have change your password successfully.')
            return redirect('my_account')
        else:
            messages.error(request, 'Password not confirm success.')
            return redirect('change_password')

    return render(request, 'auth/change_password.html')