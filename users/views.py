from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .models import User
from teams.models import Team

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # 'username' here means email due to USERNAME_FIELD
        if user is not None and user.is_approved:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'leader':
                return redirect('leader_dashboard', team_id=user.led_teams.first().id)
            elif user.role == 'member':  # Added here to handle member role
                return redirect('member_dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials or unapproved user'})
    return render(request, 'login.html')

def admin_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('login')
    users = User.objects.all()
    teams = Team.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'teams': teams})

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

def member_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'member':
        return redirect('login')
    return render(request, 'member_dashboard.html', {'user': request.user})