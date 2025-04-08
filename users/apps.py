# users/apps.py
# This sets up the users app - tells Django it’s part of the project
from django.apps import AppConfig

# Config for my users app
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # How IDs are made
    name = 'users'  # Name of the app