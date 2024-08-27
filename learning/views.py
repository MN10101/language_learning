from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Language
from .forms import ProfileForm
from django.shortcuts import render
from django.contrib import messages
from .models import Question, Answer
import random
from .forms import FileUploadForm
from .models import UserFile
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def submit_english_test(request):
    answers = request.session.get('answers', {})
    score = 0

    for question_id, selected_answer_id in answers.items():
        correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()
        if correct_answer and correct_answer.id == int(selected_answer_id):
            score += 1

    # Adjusted level determination based on the 19 questions
    if score <= 5:
        level = 'A1'
    elif score <= 10:
        level = 'A2'
    elif score <= 14:
        level = 'B1'
    elif score <= 17:
        level = 'B2'
    elif score == 18 or score == 19:
        level = 'C1'
    else:
        level = 'C2'

    # Clear session data
    request.session.flush()

    return render(request, 'test_result.html', {'score': score, 'level': level})





@login_required
def english_test(request):
    if 'question_index' not in request.session:
        # Initialize the session to track progress and randomize questions
        questions = list(Question.objects.all())
        random.shuffle(questions)
        request.session['questions'] = [q.id for q in questions]
        request.session['question_index'] = 0
        request.session['answers'] = {}

    question_index = request.session['question_index']
    question_id = request.session['questions'][question_index]
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)

    if request.method == 'POST':
        # Save the current answer
        selected_answer = request.POST.get('answer')
        if selected_answer:
            request.session['answers'][question_id] = selected_answer
            request.session['question_index'] += 1

            if request.session['question_index'] >= len(request.session['questions']):
                return redirect('submit_english_test')

            return redirect('english_test')

    context = {
        'question': question,
        'answers': answers,
        'current_number': question_index + 1,
        'total_number': len(request.session['questions']),
    }
    return render(request, 'english_test.html', context)



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
            messages.success(request, 'Profile updated successfully!')
            return redirect('view_profile')  # Redirect to 'My Profile' page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'learning/profile.html', {'form': form, 'profile': profile})



@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'learning/view_profile.html', {'profile': profile})


@login_required
def save_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('welcome')  # Redirect to the Welcome page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'learning/profile.html', {'form': form})

@login_required
def welcome(request):
    profile = request.user.profile
    return render(request, 'learning/welcome.html', {'profile': profile})



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

@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'learning/view_profile.html', {'profile': profile})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')  # Redirect to the Welcome page after login
    else:
        form = AuthenticationForm()
    return render(request, 'learning/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def choose_language(request):
    languages = Language.objects.all()
    return render(request, 'learning/choose_language.html', {'languages': languages})

def about_us(request):
    return render(request, 'learning/about_us.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)  # Don't save yet, as we need to add the user
            user_file.user = request.user        # Associate the uploaded file with the current user
            user_file.save()                     # Now save it
            messages.success(request, 'File uploaded successfully!')
            return redirect('list_files')        # Redirect after successful upload
    else:
        form = FileUploadForm()
    return render(request, 'learning/upload_file.html', {'form': form})

@login_required
def list_files(request):
    files = UserFile.objects.filter(user=request.user)
    return render(request, 'learning/list_files.html', {'files': files})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UserFile, id=file_id, user=request.user)
    if request.method == 'POST':
        file.delete()
        return redirect('list_files')