# users/views.py
# This file handles user stuff - login, admin dashboard, approving users, and member dashboard.
# It checks roles and shows the right pages for each user type.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .models import User
from teams.models import Team, TeamMember, Announcement

# Login view lets users sign in and sends them to their dashboard.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']  # Get email from form
        password = request.POST['password']  # Get password from form
        user = authenticate(request, username=email, password=password)  # Check if email/password match
        if user is None:
            return render(request, 'login.html', {'error': f'Authentication failed for {email}'})
        if not user.is_approved:
            return render(request, 'login.html', {'error': f'{email} is not approved'})
        login(request, user)  # Sign the user in
        if user.role == 'admin':
            return redirect('admin_dashboard')
        elif user.role == 'leader':
            team = user.led_teams.first()  # Get their first team
            if team:
                return redirect('leader_dashboard', team_id=team.id)
            return render(request, 'login.html', {'error': 'No team assigned to leader'})
        elif user.role == 'member':
            return redirect('member_dashboard')
    return render(request, 'login.html')  # Show login form for GET requests

# Admin dashboard shows all users and teams for admins only.
def admin_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('login')
    users = User.objects.all()  # Grab all users
    teams = Team.objects.all()  # Grab all teams
    return render(request, 'admin_dashboard.html', {'users': users, 'teams': teams})

# Approve user lets admins approve someone.
def approve_user(request, user_id):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('login')
    user = User.objects.get(id=user_id)  # Find the user by id
    user.is_approved = True  # Approve them
    user.save()  # Save the change
    return redirect('admin_dashboard')  # Go back to admin dashboard

# Member dashboard shows welcome and announcements for members.
def member_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'member':
        return redirect('login')
    team_memberships = TeamMember.objects.filter(user=request.user)  # Get teams this member is in
    team_ids = team_memberships.values_list('team_id', flat=True)  # List their team IDs
    announcements = Announcement.objects.filter(team__id__in=team_ids).order_by('-created_at')  # Get announcements
    context = {
        'user': request.user,
        'announcements': announcements,
    }
    return render(request, 'member_dashboard.html', context)