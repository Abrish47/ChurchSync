# ChurchSync: A Role-Based Church Management Platform

Hey! This is ChurchSync, a web app I built to help churches manage their members, teams, and communication better. I used Django for it, and it’s pretty solid for admins, leaders, and members to use. It’s simple but can grow bigger later if needed.

## What It Does
ChurchSync is made to:
- Let people log in safe with email and password.
- Give admins control to approve users and set up teams.
- Help leaders manage their teams (like Youth or Worship), add or remove members.
- Show a member list, but only what your role lets you see.
- Let leaders post announcements for their team to keep everyone updated.

## How to Set It Up
You’ll need Python on your computer and internet. Here’s how to get it running:

1. **Grab the Code**:  
   Open your terminal and type:
    git clone https://github.com/Abrish47/ChurchSync.git

2. **Install Stuff**:  
Get the things it needs with:
  pip install -r requirements.txt


3. **Set Up Database**:  
Tell Django to make the data space:
python manage.py migrate


4. **Make an Admin**:  
You need a main account to start. Run:
   python manage.py createsuperuser

Use something like `admin@test.com` and `testpass123` for email and password.

5. **Start It**:  
Run this:
python manage.py runserver

Then go to `http://127.0.0.1:8000/` in your browser—it’s live!

## How to Use It
- **Admin**: Log in with `admin@test.com`. You can approve people and see all teams.  
- **Leader**: Use `leader@test.com`. You manage your team, add members, post stuff.  
- **Member**: Try `member@test.com`. You get a basic view, no big controls.  
- Start at `/login/`, then check out dashboards, teams, or the member list.

## Features I Added
- **Login**: Email and password, works for everyone.  
- **Dashboards**: Different ones for admin, leader, member.  
- **Team Management**: Leaders can add or kick members from their team.  
- **Member Directory**: Shows members based on your role.  
- **Announcements**: Leaders post updates like “Meeting Sunday” for their team.  

## Extra Notes
- Built with Django and SQLite, keeps it easy to start.  
- Might have small bugs—like the list not updating fast—but it’s still good.  
- Could add more later, like events or finance stuff, but not yet.  

Thanks for checking it out! I’m happy with how it turned out. You can see it in action in my video too if you want.

