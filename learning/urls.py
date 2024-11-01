from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import CustomPasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL (Move this to the top)
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('profile/save/', views.save_profile, name='save_profile'),
    path('english-test/', views.english_test, name='english_test'),
    path('submit-test/', views.submit_english_test, name='submit_english_test'),
    path('it_test/', views.it_test, name='it_test'),
    path('submit-it-test/', views.submit_it_test, name='submit_it_test'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('about-us/', views.about_us, name='about_us'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('my-files/', views.list_files, name='list_files'),
    path('delete-file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('my-classes/', views.my_classes, name='my_classes'),
    path('my-course/', views.my_course, name='my_course'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('prices/', views.prices, name='prices'),
    path('book/<str:level>/', views.book_course, name='book_course'),
    path('success/', views.payment_success, name='success'),
    path('cancel/', views.payment_cancel, name='cancel'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('save-password-social-accounts/', views.save_password_social_accounts, name='save_password_social_accounts'),
    path('save-time-language/', views.save_time_language, name='save_time_language'),
    path('save-notifications/', views.save_notifications, name='save_notifications'),
    path('save-calendar-connection/', views.save_calendar_connection, name='save_calendar_connection'),
    path('chatbot-answer/', views.chatbot_answer, name='chatbot_answer'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
    path('soft_skills/', views.soft_skills, name='soft_skills'),
    
    # Password Reset URLs
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Game-related URLs for teachers
    path('students/', views.students_view, name='students'),
    path('game/', views.game, name='game'),
    path('game2/', views.game2, name='game2'),
    path('game3/', views.game3, name='game3'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('games/', views.games_page, name='games_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
