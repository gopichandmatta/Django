# Django User Authentication and Email Sending

This Django project provides user authentication functionality including registration, login, logout, and profile views. Additionally, it allows users to send emails.

## Installation

1. Clone this repository.
2. Install Django if not already installed: `pip install django`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.

## Usage

- Access the home page at `/` to see the main page.
- Register a new user by visiting `/register/`.
- Log in to an existing account at `/login/`.
- Send emails via `/send-email/`.
- Access the user profile at `/profile/`.
- Log out from the current session at `/logout/`.

## URL Patterns

The project uses the following URL patterns:

- `/`: Home page.
- `/register/`: User registration page.
- `/login/`: User login page.
- `/send-email/`: Page for sending emails.
- `/logout/`: Logout page.
- `/profile/`: User profile page.

## Views

- `Home`: Displays the home page.
- `RegisterUser`: Handles user registration.
- `UserLogin`: Handles user login.
- `SendEmail`: Handles sending emails.
- `LogoutUser`: Logs out the current user.
- `profile`: Displays the user profile.

## Files

- `models.py`: Defines the UserProfile model.
- `forms.py`: Contains forms for user registration, login, and sending emails.
- `views.py`: Defines view functions and classes.
- `serializers.py`: Contains serializers for user-related models.

## URLs

URL patterns are defined in `urls.py`.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
