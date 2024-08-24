from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import save_profile, english_test, submit_english_test

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
]
