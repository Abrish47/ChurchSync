# users/admin.py
# This sets up how admins see and manage users in the admin site
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Custom admin setup for my User model
class UserAdmin(BaseUserAdmin):
    # What shows in the user list
    list_display = ('email', 'role', 'is_approved', 'is_active')  # Columns to see
    list_filter = ('role', 'is_approved', 'is_active')  # Filter options
    search_fields = ('email',)  # Search by email
    
    # What shows when editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # Basic login stuff
        ('Personal Info', {'fields': ('first_name', 'last_name')}),  # Name fields
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role', 'is_approved')}),  # Control access
    )
    # What shows when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Makes form wider
            'fields': ('email', 'password1', 'password2', 'role', 'is_approved'),  # Fields to fill
        }),
    )
    ordering = ('email',)  # Sort by email

# Hook it up to the admin site
admin.site.register(User, UserAdmin)