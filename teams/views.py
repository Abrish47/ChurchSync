from django.shortcuts import render
from django.shortcuts import redirect
from .models import TeamMember
from .models import Team, Announcement
from users.models import User

# Create your views here.
def leader_dashboard(request, team_id):
    if not request.user.is_authenticated or request.user.role != 'leader':
        return redirect('login')
    team = Team.objects.get(id=team_id, leader=request.user)
    team_members = TeamMember.objects.filter(team=team)
    return render(request, 'leader_dashboard.html', {'team': team, 'team_members': team_members})

def member_directory(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role == 'admin':
        members = User.objects.filter(is_approved=True)
    elif request.user.role == 'leader':
        team = request.user.led_teams.first()
        members = User.objects.filter(teammember__team=team, is_approved=True)
    else:
        members = []
    return render(request, 'member_directory.html', {'members': members})

def announcements(request, team_id):
    if not request.user.is_authenticated or request.user.role != 'leader':
        return redirect('login')
    team = Team.objects.get(id=team_id, leader=request.user)
    if request.method == 'POST':
        content = request.POST['content']
        Announcement.objects.create(team=team, content=content, posted_by=request.user)
    announcements = Announcement.objects.filter(team=team).order_by('-created_at')
    return render(request, 'announcements.html', {'team': team, 'announcements': announcements})