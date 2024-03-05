from django.urls import path
from .views import (StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
                    UserRegistrationView, UserLoginView)

urlpatterns = [
    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),  # URL for student list
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),  # URL for student detail
    path('students/create/', StudentCreateView.as_view(), name='student_create'),  # URL for creating a student
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),  # URL for updating a student
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),  # URL for deleting a student
    path('register/', UserRegistrationView.as_view(), name='register'),  # URL for user registration
    path('login/', UserLoginView.as_view(), name='login'),  # URL for user login
]
