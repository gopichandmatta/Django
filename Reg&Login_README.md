Project Structure <a name="project-structure"></a>
Describe the structure of your Django project, including directories, files, and their purposes.
project/
├── email_sender_app/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── profile.html
│   ├── register.html
│   └── send_email.html
└── manage.py


Functionalities <a name="functionalities"></a>
Explain the main functionalities of the project, such as user registration, login, sending emails, and viewing profiles.

User Registration: Allows users to register for an account by providing a username, email, and password.
User Login: Allows registered users to log in using their username and password.
Sending Emails: Allows users to send emails by providing the recipient's email address, subject, and message.
Viewing Profiles: Displays the user's profile page with their username and a welcome message.
Views <a name="views"></a>
Provide descriptions of the views in your project and their functionalities.

Home: Displays the home page with options to register or login.
RegisterUser: Handles user registration by rendering the registration form and saving user data to the database.
UserLogin: Handles user login by rendering the login form, authenticating users, and redirecting to the profile page upon successful login.
SendEmail: Allows users to send emails by rendering the email form and sending emails using Django's send_mail function.
LogoutUser: Logs out the user and redirects to the login page.
Models <a name="models"></a>
Describe the models used in your project and their relationships.

UserProfile: Represents user profiles with a one-to-one relationship with the built-in User model. It includes a bio field for additional user information.
Forms <a name="forms"></a>
Explain the forms used in your project and their purposes.

UserRegistrationForm: Allows users to register by providing a username, email, and password.
UserLoginForm: Allows users to log in by providing a username and password.
EmailForm: Allows users to send emails by providing the recipient's email address, subject, and message.
URLs <a name="urls"></a>
List the URLs and their associated views in your project.

/: Home page (Home view)
/register/: User registration page (RegisterUser view)
/login/: User login page (UserLogin view)
/send-email/: Send email page (SendEmail view)
/logout/: Logout page (LogoutUser view)
/profile/: User profile page (profile view)
Templates <a name="templates"></a>
Provide descriptions of the templates used in your project and their purposes.

base.html: Base template containing the common structure for all other templates.
home.html: Home page template with options to register or login.
register.html: User registration form template.
login.html: User login form template.
send_email.html: Email form template.
profile.html: User profile page template displaying the user's username and a welcome message.
