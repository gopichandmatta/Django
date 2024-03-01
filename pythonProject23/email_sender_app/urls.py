# email_sender_app/urls.py

from django.urls import path
from .views import RegisterUser, UserLogin, SendEmail, profile, Home, LogoutUser

urlpatterns = [

    path('', Home.as_view(), name='home'), # Home page
    path('register/', RegisterUser.as_view(), name='register'),# User registration page
    path('login/', UserLogin.as_view(), name='login'),# User login page
    path('send-email/', SendEmail.as_view(), name='send_email'),# Send email page
    path('logout/', LogoutUser.as_view(), name='logout'),# Logout page
    path('profile/', profile, name='profile'),# User profile page
]
