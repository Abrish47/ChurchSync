# This file has views for team stuff - leader dashboard, member directory, and announcements.
# It pulls data from models and shows it based on user roles.
from django.shortcuts import render
from django.shortcuts import redirect
from .models import TeamMember
from .models import Team, Announcement
from users.models import User

# Leader dashboard shows team info for leaders only.
def leader_dashboard(request, team_id):
    # Check if user is logged in and a leader, else send them to login
    if not request.user.is_authenticated or request.user.role != 'leader':
        return redirect('login')
    # Get the team this leader owns by its id
    team = Team.objects.get(id=team_id, leader=request.user)
    # Grab all members in this team
    team_members = TeamMember.objects.filter(team=team)
    # Send team and member info to the template
    return render(request, 'leader_dashboard.html', {'team': team, 'team_members': team_members})

# Member directory shows approved users based on who's looking.
def member_directory(request):
    # If not logged in, go to login page
    if not request.user.is_authenticated:
        return redirect('login')
    # Admins see all approved users
    if request.user.role == 'admin':
        members = User.objects.filter(is_approved=True)
    # Leaders see approved members in their team
    elif request.user.role == 'leader':
        team = request.user.led_teams.first()  # Get leader's first team
        members = User.objects.filter(teammember__team=team, is_approved=True)
    # Members see nothing for now
    else:
        members = []
    # Send member list to the template
    return render(request, 'member_directory.html', {'members': members})

# Announcements lets leaders post and see messages for their team.
def announcements(request, team_id):
    # Only leaders can use this, else go to login
    if not request.user.is_authenticated or request.user.role != 'leader':
        return redirect('login')
    # Get the team this leader runs
    team = Team.objects.get(id=team_id, leader=request.user)
    # If leader submits a new announcement
    if request.method == 'POST':
        content = request.POST['content']  # Grab the message text
        # Save it with team and who posted it
        Announcement.objects.create(team=team, content=content, posted_by=request.user)
    # Get all announcements for this team, newest first
    announcements = Announcement.objects.filter(team=team).order_by('-created_at')
    # Show them in the template
    return render(request, 'announcements.html', {'team': team, 'announcements': announcements})