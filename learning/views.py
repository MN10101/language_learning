from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Language

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'learning/profile.html', {'form': form})


def home(request):
    return render(request, 'learning/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'learning/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'learning/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def choose_language(request):
    languages = Language.objects.all()
    return render(request, 'learning/choose_language.html', {'languages': languages})
