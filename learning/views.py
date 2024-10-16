from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.urls import reverse
import stripe
import pytz
import random
import openai
import json
import logging
from django.http import JsonResponse
from .models import Teacher, Language, Question, Answer, UserFile, ScheduledClass, Course
from .forms import ProfileForm, FileUploadForm

stripe.api_key = settings.STRIPE_SECRET_KEY


# openai.api_key = settings.OPENAI_API_KEY

# # Initialize logger for debugging
# logger = logging.getLogger(__name__)



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
    # Ensure test questions are filtered properly
    test_questions = Question.objects.filter(category='test') 

    if 'question_index' not in request.session or 'questions' not in request.session:
        # Initialize the session to track progress and randomize questions
        questions = list(test_questions)
        random.shuffle(questions)
        request.session['questions'] = [q.id for q in questions]
        request.session['question_index'] = 0
        request.session['answers'] = {}

    # Retrieve the current question index
    question_index = request.session.get('question_index', 0)  # Default to 0 if not set
    questions = request.session.get('questions', [])

    # Check if there are questions available
    if not questions or question_index >= len(questions):
        # Redirect to the test result page if there are no more questions
        return redirect('submit_english_test')

    question_id = questions[question_index]
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)

    if request.method == 'POST':
        # Save the current answer
        selected_answer = request.POST.get('answer')
        if selected_answer:
            request.session['answers'][question_id] = selected_answer
            request.session['question_index'] += 1

            # Check if we've reached the end of the questions
            if request.session['question_index'] >= len(questions):
                return redirect('submit_english_test')

            return redirect('english_test')

    context = {
        'question': question,
        'answers': answers,
        'current_number': question_index + 1,
        'total_number': len(questions),
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
            return redirect('view_profile')  # Redirect to a view that shows the updated profile
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'learning/profile.html', {
        'form': form,
        'profile': profile,
    })




@login_required
def view_profile(request):
    profile = request.user.profile

    # Check if the profile picture exists; if not, assign a default image
    profile_picture_url = profile.profile_picture.url if profile.profile_picture else '/media/profile_pictures/default_profile_picture.png'
    
    return render(request, 'learning/view_profile.html', {
        'profile': profile,
        'profile_picture_url': profile_picture_url
    })


@login_required
def save_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('welcome')
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
            user = form.save()

            # Check if the registration is for a teacher (you could add a condition here)
            if request.POST.get('is_teacher'):
                teachers_group, created = Group.objects.get_or_create(name='Teachers')
                user.groups.add(teachers_group)

                # Optionally, create the Teacher profile
                Teacher.objects.create(user=user)
            else:
                # Automatically add the new user to the 'Students' group
                students_group, created = Group.objects.get_or_create(name='Students')
                user.groups.add(students_group)

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'learning/register.html', {'form': form})


@login_required
def view_profile(request):
    profile = request.user.profile
    is_teacher = request.user.groups.filter(name='Teachers').exists()

    # Check if the profile picture exists; if not, assign a default image
    profile_picture_url = profile.profile_picture.url if profile.profile_picture else '/media/profile_pictures/default_profile_picture.png'

    return render(request, 'learning/view_profile.html', {
        'profile': profile,
        'is_teacher': is_teacher,
        'profile_picture_url': profile_picture_url
    })



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome') 
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
            user_file = form.save(commit=False) 
            user_file.user = request.user  
            user_file.save()         
            messages.success(request, 'File uploaded successfully!')
            return redirect('list_files')   
    else:
        form = FileUploadForm()
    return render(request, 'learning/upload_file.html', {'form': form})

@login_required
def list_files(request):
    files = UserFile.objects.filter(user=request.user)
    
    # Convert the uploaded_at field to Berlin time for each file
    berlin_tz = pytz.timezone('Europe/Berlin')
    for file in files:
        file.uploaded_at_berlin = timezone.localtime(file.uploaded_at, berlin_tz)
    
    return render(request, 'learning/list_files.html', {'files': files})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UserFile, id=file_id, user=request.user)
    if request.method == 'POST':
        file.delete()
        return redirect('list_files')
    
@login_required
def my_classes(request):
    classes = ScheduledClass.objects.filter(user=request.user).order_by('scheduled_time')
    return render(request, 'learning/my_classes.html', {'classes': classes})


@login_required
def my_course(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'learning/my_course.html', {'courses': courses})



def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Debugging line to check the type of settings
        print(f"Type of settings: {type(settings)}")  # Add this line

        send_mail(
            f'Message from {name} via Contact Us',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')
    return render(request, 'learning/contact_us.html')




def book_course(request, level):
    course_prices = {
        'A1': 20000,
        'A2': 25000,
        'B1': 30000,
        'B2': 35000,
        'C1': 40000,
        'C2': 45000,
        'Business-Intermediate': 50000,
        'Business-Advanced': 60000,
    }

    # Get the price in cents and convert it to euros
    price = course_prices.get(level, 0) / 100 

    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': f'{level} Course',
                    },
                    'unit_amount': course_prices[level],
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
        return redirect(session.url, code=303)

    return render(request, 'learning/book_course.html', {'level': level, 'price': price})


def prices(request):
    # Define prices for different levels
    course_prices = {
        'A1': 20000,
        'A2': 25000,
        'B1': 30000,
        'B2': 35000,
        'C1': 40000,
        'C2': 45000,
        'Business-Intermediate': 50000,
        'Business-Advanced': 60000,
    }
    
    context = {
        'course_prices': course_prices
    }
    
    return render(request, 'learning/prices.html', context)

def payment_success(request):
    return render(request, 'learning/payment_success.html')

def payment_cancel(request):
    return render(request, 'learning/payment_cancel.html')

def teachers_view(request):
    # Fetch all teachers who have been added by admin
    teachers = Teacher.objects.select_related('user').all()
    
    # Debugging output to check if teachers are being fetched
    print(teachers)
    
    return render(request, 'learning/teachers.html', {'teachers': teachers})



def save_password_social_accounts(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            # Assuming you have access to the user object
            user = request.user
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password successfully updated.')
            else:
                messages.error(request, 'Current password is incorrect.')
        else:
            messages.error(request, 'New passwords do not match.')

    return redirect('settings')

def save_time_language(request):
    if request.method == 'POST':
        timezone = request.POST.get('timezone')
        time_format = request.POST.get('time_format')
        week_start = request.POST.get('week_start')
        site_language = request.POST.get('site_language')

        # Assuming you have a profile model related to the user
        user_profile = request.user.profile
        user_profile.timezone = timezone
        user_profile.time_format = time_format
        user_profile.week_start = week_start
        user_profile.site_language = site_language
        user_profile.save()

        messages.success(request, 'Time and language settings saved.')
    
    return redirect('settings')

@login_required
def save_notifications(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        
        # Update the profile with POST data, setting checkboxes to False if not present
        user_profile.system_notifications = request.POST.get('system_notifications', False)
        user_profile.one_click_booking = request.POST.get('one_click_booking', False)
        user_profile.next_class_notification = request.POST.get('next_class_notification', False)
        user_profile.email_notifications = request.POST.get('email_notifications', False)
        user_profile.booked_class_confirmation = request.POST.get('booked_class_confirmation', False)
        user_profile.cancelled_class_confirmation = request.POST.get('cancelled_class_confirmation', False)
        user_profile.marketing_communications = request.POST.get('marketing_communications', False)
        user_profile.class_reminder = request.POST.get('class_reminder', False)
        user_profile.weekly_recap = request.POST.get('weekly_recap', False)

        user_profile.save()
        messages.success(request, 'Notification settings saved.')
    
    return redirect('settings')


def save_calendar_connection(request):
    if request.method == 'POST':
        # This may involve redirecting the user to an OAuth page for Google or Office365
        messages.success(request, 'Calendar connection settings saved.')
    
    return redirect('settings')


# Check if the user is in the 'Teachers' group
def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()

@login_required
@user_passes_test(is_teacher)
def game(request):
    game_questions = Question.objects.filter(category='game') 
    print(game_questions) 
    return render(request, 'game.html', {'questions': game_questions})



@login_required
@user_passes_test(is_teacher)
def game2(request):
    return render(request, 'game2.html')

@login_required
@user_passes_test(is_teacher)
def game3(request):
    return render(request, 'game3.html')


# Check if the user is in the 'Teachers' group
def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()



@login_required
@user_passes_test(is_teacher)
def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question) 
    
    context = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'question.html', context)


def get_questions():
    return Question.objects.all()

@login_required
@user_passes_test(is_teacher)
def students_view(request):
    # Retrieve students who are not staff (i.e., not admin) and have booked classes
    students = User.objects.filter(groups__name='Students').exclude(is_staff=True).distinct()

    # Get profile information and booked classes for each student
    student_profiles = []
    for student in students:
        profile = student.profile 
        booked_classes = ScheduledClass.objects.filter(user=student).distinct()
        student_profiles.append({
            'student': student,
            'profile': profile,
            'booked_classes': booked_classes
        })

    context = {
        'student_profiles': student_profiles,
    }

    return render(request, 'learning/students.html', context)

# @csrf_exempt
# def chatbot_answer(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_question = data.get('question', '')

#         if not user_question:
#             return JsonResponse({'error': 'No question provided'}, status=400)

#         try:
#             # Call GPT-3.5 or GPT-4 from OpenAI
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # or "gpt-4"
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": user_question},
#                 ],
#                 max_tokens=150
#             )
#             chatbot_answer = response['choices'][0]['message']['content']
#             return JsonResponse({'answer': chatbot_answer})

#         except openai.error.RateLimitError:
#             return JsonResponse({'error': 'OpenAI API rate limit exceeded. Please try again later.'}, status=429)

#         except openai.error.AuthenticationError:
#             return JsonResponse({'error': 'Invalid OpenAI API key.'}, status=500)

#         except Exception as e:
#             return JsonResponse({'error': f'General error: {str(e)}'}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def chatbot_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_question = data.get('question', '').lower().strip()

        if not user_question:
            return JsonResponse({'error': 'No question provided'}, status=400)

        # Define some common questions and answers
        responses = {
        "hello": "Hello! How can I help you today?",
        "what is this app?": "This app is a language learning platform where you can take quizzes, schedule classes, and track your progress.",
        "how do i register?": "You can register by clicking on the 'Register' button at the top right corner of the homepage and filling out your details.",
        "how can i book a course?": "To book a course, go to the 'Book Course' page, select your level, and follow the payment instructions.",
        "who are the teachers?": "Our teachers are experienced professionals who are passionate about helping you learn languages.",
        "what languages can i learn?": "Currently, we offer courses in English, Spanish, French, and German.",
        "how do i reset my password?": "You can reset your password by clicking the 'Forgot Password' link on the login page.",
        "how can i contact support?": "You can reach our support team by using the 'Contact Us' page or emailing us at support@example.com.",
        "what are the payment options?": "We accept credit card payments through Stripe. All transactions are secure and encrypted.",
        "how can i update my profile?": "You can update your profile by navigating to the 'Profile' section and clicking 'Edit'.",
        "what is the refund policy?": "You can request a refund within 14 days of purchase if you have not started the course.",
        "can i change my course level?": "Yes, you can change your course level by contacting support or directly on the course settings page.",
        "how long does each course take?": "Each course is designed to be flexible, but the average course takes about 4 to 6 weeks to complete.",
        "can i access the course on mobile?": "Yes, you can access the courses from your mobile device using any browser. The app is fully responsive for mobile use.",
        "do you offer certificates?": "Yes, upon completing a course, you will receive a certificate of completion that you can download and share.",
        "how much does a course cost?": "Course prices vary depending on the level. Please visit the 'Prices' page for the most up-to-date pricing information.",
        "can i take more than one course at a time?": "Yes, you can enroll in multiple courses at the same time, depending on your availability and schedule.",
        "are the lessons live or pre-recorded?": "Our courses include a mix of pre-recorded video lessons, quizzes, and live classes with instructors.",
        "can i interact with other students?": "Yes, we encourage interaction between students. You can join group discussions, study groups, and participate in class forums.",
        "what happens if i miss a live class?": "If you miss a live class, don't worry! Recordings of the sessions are available for you to watch at any time.",
        "do you offer a free trial?": "Yes, we offer a free trial for certain courses. Please check the course details page to see if a trial is available.",
        "how can i cancel my subscription?": "You can cancel your subscription by going to the 'Account Settings' page and clicking on 'Manage Subscription'.",
        "is there a discount for bulk courses?": "Yes, we offer discounts for bulk course purchases or for businesses looking to enroll multiple employees. Contact our support team for more information.",
        "how do i schedule a live class?": "You can schedule a live class by visiting the 'My Classes' section and selecting an available time slot.",
        "can i change my scheduled class?": "Yes, you can reschedule or cancel a class up to 24 hours before the class starts. Go to 'My Classes' to manage your bookings.",
        "are there quizzes in the course?": "Yes, each course includes quizzes to test your knowledge and help reinforce the material.",
        "what is the grading system?": "Our grading system is based on quiz scores, class participation, and your overall engagement with the course materials.",
        "can i get a tutor for one-on-one sessions?": "Yes, we offer personalized one-on-one tutoring sessions for students who want additional help.",
        "how do i apply a discount code?": "You can apply a discount code during the checkout process in the 'Payment' section.",
        "where can i see my progress?": "You can view your progress by going to the 'My Course' page where you'll find your completed lessons, scores, and upcoming classes.",
        "can i download course materials?": "Yes, course materials such as worksheets and slides can be downloaded directly from the lesson pages.",
        "how can i refer a friend?": "You can refer a friend by sharing your unique referral link, which can be found in the 'Profile' section under 'Referrals'.",
        "is there a loyalty program?": "Yes, we have a loyalty program where you earn points for completing courses, attending live classes, and referring friends. Points can be redeemed for discounts.",
        "what level should i start at?": "If you're unsure about your level, we recommend taking our placement test, available on the homepage, to find the best course for you.",
        "can i learn at my own pace?": "Yes, you can learn at your own pace. While live classes have scheduled times, the video lessons and quizzes can be completed anytime.",
        "do i need to buy books or materials?": "All materials are included in the course, and additional reading or worksheets can be downloaded from the lesson pages.",
        "how do i improve my speaking skills?": "To improve your speaking skills, we recommend participating in live classes, scheduling one-on-one tutoring, or joining student discussion groups.",
        "how much time should i spend learning each day?": "We suggest dedicating at least 30 minutes a day to your studies, but you can adjust this based on your own pace and goals.",
        "are there any practice exercises?": "Yes, each course includes exercises and practice quizzes designed to help reinforce what you've learned.",
        "how do live classes work?": "Live classes are held via video conferencing. You can participate in real-time, ask questions, and interact with the instructor and other students.",
        "what happens after i complete a course?": "After completing a course, you will receive a certificate, and you can move on to the next level or continue learning with more advanced topics.",
        "how do i track my daily streak?": "Your daily streak is tracked on your dashboard. Keep logging in and completing lessons daily to maintain your streak!",
        "do i need to have a webcam for live classes?": "A webcam is recommended for live classes so you can fully engage with the instructor, but it's not mandatory.",
        "how do i stay motivated?": "Try setting small, achievable goals and reward yourself for meeting them! You can also join group discussions or study with friends to stay engaged.",
        "i'm not making progress, what should i do?": "It can feel frustrating when you're not making progress, but try to review past lessons, focus on weak areas, and don’t hesitate to reach out to a tutor for extra help.",
        "how can i fit learning into my busy schedule?": "Our courses are flexible. You can schedule live classes when it's convenient, and complete lessons and quizzes on your own time, even if it’s just 10 minutes a day.",
        "can i study offline?": "At the moment, our courses are fully online. However, you can download certain materials like worksheets to use offline.",
        "can i get feedback on my progress?": "Absolutely! Instructors provide feedback in live classes, and our system tracks your performance on quizzes and exercises, so you know where to improve."
    }



        # Default response if the question is not recognized
        default_response = "I'm sorry, I didn't understand that. Can you please rephrase?"

        # Get the response for the user question, or use the default response
        chatbot_answer = responses.get(user_question, default_response)
        return JsonResponse({'answer': chatbot_answer})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')