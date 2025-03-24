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
        user = authenticate(request, username=email, password=password)  # 'username' here means email
        if user is not None and user.is_approved:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'leader':
                return redirect('leader_dashboard', team_id=user.led_teams.first().id)
            else:
                return redirect('login')  # Members redirect back for now
        return render(request, 'login.html', {'error': 'Invalid credentials or unapproved user'})
    return render(request, 'login.html')

def admin_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('login')
    users = User.objects.all()
    teams = Team.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'teams': teams})