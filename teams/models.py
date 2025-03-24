from django.db import models
from users.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_teams')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'team')  # No duplicate memberships

    def __str__(self):
        return f"{self.user.email} in {self.team.name}"
    
class Announcement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content[:20]}... by {self.posted_by.email}"