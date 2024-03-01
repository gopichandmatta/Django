from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserLoginForm, EmailForm

class RegisterUserTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_user_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_user_form_valid_data(self):
        response = self.client.post(reverse('register'), {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Should redirect to profile page upon successful registration

class UserLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_login_form_valid_data(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Should redirect to profile page upon successful login

class SendEmailTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_send_email_view(self):
        response = self.client.get(reverse('send_email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_email.html')

    def test_send_email_form_valid_data(self):
        response = self.client.post(reverse('send_email'), {'to_email': 'recipient@example.com', 'subject': 'Test Subject', 'message': 'Test Message'})
        self.assertEqual(response.status_code, 302)  # Should redirect to success page upon successful email sending
