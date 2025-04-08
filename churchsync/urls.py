"""
URL configuration for churchsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL config for churchsync project.

This list connects URLs to views - like a map for the site
"""
from django.contrib import admin
from django.urls import path
from users.views import login_view, approve_user
from users.views import admin_dashboard, member_dashboard
from teams.views import leader_dashboard, member_directory
from teams.views import announcements
from django.contrib.auth import views as auth_views

# List of all URLs and where they go
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('login/', login_view, name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout and back to login
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('dashboard/teams/<int:team_id>/', leader_dashboard, name='leader_dashboard'),  # Leader dashboard with team ID
    path('directory/', member_directory, name='member_directory'),  # Member list page
    path('teams/<int:team_id>/announcements/', announcements, name='announcements'),  # Team announcements
    path('dashboard/member/', member_dashboard, name='member_dashboard'),  # Member dashboard
    path('approve/<int:user_id>/', approve_user, name='approve_user'),  # Approve a user by ID
]