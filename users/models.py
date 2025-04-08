# This file sets up the User model - how users are stored and managed.
# It changes Django’s default user to use email instead of username.
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager

# Custom manager to handle making users
class UserManager(BaseUserManager):
    # Makes a regular user with email and password
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')  # Email can’t be empty
        email = self.normalize_email(email)  # Fix email format
        user = self.model(email=email, **extra_fields)  # Create user object
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save to database
        return user

    # Makes a superuser (like admin) with extra powers
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Can use admin site
        extra_fields.setdefault('is_superuser', True)  # Full control
        extra_fields.setdefault('is_approved', True)  # Auto-approved
        extra_fields.setdefault('role', 'admin')  # Set as admin
        # Check superuser needs
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)  # Make the user

# My custom User model
class User(AbstractUser):
    username = None  # No username - using email instead
    email = models.EmailField(unique=True)  # Email is the ID, no repeats
    # Role picks admin, leader, or member
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('leader', 'Leader'), ('member', 'Member')], default='member')
    is_approved = models.BooleanField(default=False)  # New users need approval

    objects = UserManager()  # Use my manager

    USERNAME_FIELD = 'email'  # Login with email
    REQUIRED_FIELDS = []  # Just email and password needed

    def __str__(self):
        return self.email  # Show email when printing user