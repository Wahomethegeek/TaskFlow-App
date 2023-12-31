from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# import Django messages (notifications)
from django.contrib import messages
from .models import Task


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

            messages.success(request, "User created successfully")

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
    return render(request, 'profile/dashboard.html')


# profile
@login_required(login_url='my-login')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')

    # setting a unique instance based on the user logged in
    user_form = UpdateUserForm(instance=request.user)

    context = {'user_form': user_form}

    return render(request, 'profile/profile.html', context=context)


@login_required(login_url='my-login')
def deleteProfile(request):
    if request.method == 'POST':
        delete_user = User.objects.get(username=request.user)

        delete_user.delete()

        return redirect('')
    return render(request, 'profile/delete-account.html')


# Create a task
@login_required(login_url="my-login")
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect("view_task")

    context = {'form': form}
    return render(request, 'profile/create-task.html', context=context)


# View all Tasks
@login_required(login_url='my-login')
def viewTask(request):
    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task': task}

    return render(request, 'profile/view-task.html', context=context)


# update a task
@login_required(login_url='my-login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect("view_task")

    context = {'form': form}

    return render(request, 'profile/update-task.html', context=context)


# Delete task
@login_required(login_url='my-login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect("view_task")

    return render(request, 'profile/delete-task.html')


# Logout a user
def my_logout(request):
    auth.logout(request)

    return redirect('')
