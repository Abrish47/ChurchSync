# This file sets up models for teams - teams, members, and announcements.
# It connects users to teams and stores messages.
from django.db import models
from users.models import User

# Team model for groups in the church
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Team name, no repeats
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_teams')  # Who runs it

    def __str__(self):
        return self.name  # Show team name when printing

# Links users to teams
class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The member
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # Their team

    class Meta:
        unique_together = ('user', 'team')  # No duplicate memberships

    def __str__(self):
        return f"{self.user.email} in {self.team.name}"  # Show who’s in what team

# Stores messages for teams
class Announcement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # Which team it’s for
    content = models.TextField()  # The message
    created_at = models.DateTimeField(auto_now_add=True)  # When it was posted
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Who wrote it

    def __str__(self):
        return f"{self.content[:20]}... by {self.posted_by.email}"  # Short preview of message