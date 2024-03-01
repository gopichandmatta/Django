from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserLoginForm, EmailForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User


@login_required
def profile(request):
    """View for user profile."""
    username = request.user.username  # Get the username of the current user
    return render(request, 'profile.html', {'username': username})


class Home(View):
    """View for home page."""

    def get(self, request):
        return render(request, "home.html")


class RegisterUser(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user data to the database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('/login/')
        return render(request, 'register.html', {'form': form})


class UserLogin(View):
    """View for user login."""

    def get(self, request):
        """GET method for displaying login form."""
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        """POST method for processing login form."""
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                form.add_error(None, 'Invalid username or password')

        return render(request, 'login.html', {'form': form})


class SendEmail(View):
    """View for sending emails."""

    def get(self, request):
        """GET method for displaying email form."""
        form = EmailForm()
        return render(request, 'send_email.html', {'form': form})

    def post(self, request):
        """POST method for processing email form."""
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'your_email@example.com', [to_email])
            return HttpResponseRedirect('/success/')
        return render(request, 'send_email.html', {'form': form})


class LogoutUser(View):
    """View for user logout."""

    def get(self, request):
        """GET method for logging out user."""
        logout(request)
        return HttpResponseRedirect('/login/')
