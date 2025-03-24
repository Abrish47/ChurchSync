from django.shortcuts import render
from django.shortcuts import redirect
from .models import TeamMember
from .models import Team

# Create your views here.
def leader_dashboard(request, team_id):
    if not request.user.is_authenticated or request.user.role != 'leader':
        return redirect('login')
    team = Team.objects.get(id=team_id, leader=request.user)
    team_members = TeamMember.objects.filter(team=team)
    return render(request, 'leader_dashboard.html', {'team': team, 'team_members': team_members})