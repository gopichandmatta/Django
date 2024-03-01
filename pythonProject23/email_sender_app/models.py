from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Model representing user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        """String representation of the user profile."""
        return self.user.username
