# teams/admin.py
from django.contrib import admin
from .models import Team, TeamMember, Announcement  

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Announcement)