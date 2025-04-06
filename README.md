# ChurchSync: A Role Base Church Manage Platform

Hello! This ChurchSync, a web app I make to help church people manage their member, team, and talk easy. I build it with Django, it work good for church leader, admin, and member. It simple but strong, can grow big later if want.

## What it Do
ChurchSync help church to:
- Login safe with email and password.
- Give admin power to check new people and make team.
- Let leader handle their team like Youth or Worship, add or remove member.
- Show member list but only what you allow to see.
- Post message for team so everyone know what happen.

## How to Setup
You need computer with Python and internet. Follow this step:

1. **Get the Code**:  
   Type this in your computer terminal:
     git clone https://github.com/Abrish47/ChurchSync.git

2. **Install Things**:  
You need some Python stuff. Type:
pip install -r requirements.txt

It get all thing app need.

3. **Make Database**:  
Tell Django to set up place for data:
python manage.py migrate


4. **Make Admin**:  
You need boss account to start. Type:
 python manage.py createsuperuser

Put email like `admin@test.com` and password like `testpass123`.

5. **Run App**:  
Start it with:
python manage.py runserver

Then open browser, go `http://127.0.0.1:8000/`. It work!

## How to Use
- **Admin**: Login with boss account (`admin@test.com`). You see all team, approve new people.  
- **Leader**: Login like `leader@test.com`. You only see your team, add member, post message.  
- **Member**: Login like `member@test.com`. You see small thing, no big power.  
- Go `/login/` to start, then play with dashboard, team, and list.

## Feature I Make
- **Login**: Use email and password, safe for all.  
- **Dashboard**: Different for admin, leader, member.  
- **Team Work**: Leader can add or kick member in their team.  
- **Member List**: Show people but only what your role can see.  
- **Message**: Leader post news for team, like “Meeting Sunday”.  

## Note
- I use Django and SQLite, it easy to start.  
- Some small problem maybe there, like list not fast update, but it still good.  
- Can add more later, like event or money thing, but not now.  

Thank you! This my project, I happy it work. Check my video too if you want see it live!
