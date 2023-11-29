from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # queryset = Task.objects.all()

    return render(request, 'index.html')


# Register a user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    context = {'form': form}

    return render(request, 'register.html', context=context)


# Login a User
def my_login(request):
    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'login.html', context=context)


# Dashboard page
@login_required(login_url='my-login')  # decorator to protect our view
def dashboard(request):
    return render(request, 'dashboard.html')


# Logout a user
def my_logout(request):
    auth.logout(request)

    return redirect('')
