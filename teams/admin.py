# teams/admin.py
# This sets up how teams, members, and announcements show in the admin site
from django.contrib import admin
from .models import Team, TeamMember, Announcement  

# Add these to the admin site so I can manage them
admin.site.register(Team)  # Teams list
admin.site.register(TeamMember)  # Team members list
admin.site.register(Announcement)  # Announcements list