from django import forms


class UserRegistrationForm(forms.Form):
    """Form for user registration."""
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    """Form for user login."""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class EmailForm(forms.Form):
    """Form for sending emails."""
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)