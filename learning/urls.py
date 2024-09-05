from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('profile/save/', views.save_profile, name='save_profile'),
    path('english-test/', views.english_test, name='english_test'),
    path('submit-test/', views.submit_english_test, name='submit_english_test'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('settings/', views.settings, name='settings'),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

