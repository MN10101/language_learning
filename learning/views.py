from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Language
from .forms import ProfileForm
from django.shortcuts import render

def submit_english_test(request):
    if request.method == 'POST':
        # Process form data here
        score = calculate_score(request.POST)  # Assume calculate_score is your function to compute the score
        return render(request, 'test_result.html', {'score': score})
    else:
        # Handle GET or other methods if necessary
        return render(request, 'some_other_template.html')

@login_required
def english_test(request):
    return render(request, 'english_test.html')

@login_required
def submit_english_test(request):
    if request.method == 'POST':
        # Process answers and evaluate the test
        q1_answer = request.POST.get('q1')
        q2_answer = request.POST.get('q2')
        
        # Simple example of evaluating answers
        score = 0
        if q1_answer.lower() == 'went':
            score += 1
        if q2_answer == 'b':
            score += 1
        
        # Store score or provide feedback (this example just prints the score)
        return render(request, 'test_result.html', {'score': score})




@login_required
def settings(request):
    return render(request, 'learning/settings.html')

@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'learning/profile.html', {'form': form, 'profile': profile})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

@login_required
def save_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('english_test')  # Redirect to the English test page
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'profile.html', {'form': form})

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
