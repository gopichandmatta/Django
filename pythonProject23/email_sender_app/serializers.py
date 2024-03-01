from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_Kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Method to create a new user."""
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile model."""
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = ['user', 'bio']