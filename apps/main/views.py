from django.shortcuts import render, redirect,reverse
from django.contrib import messages
import bcrypt
import re
from .models import User
import datetime

REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,'main/index.html')

def register(request):
    name=request.POST['html_name']
    email=request.POST['html_email']
    username=request.POST['html_username']
    password=request.POST['html_password']
    password_confirm=request.POST['html_confirm']
    date=request.POST['html_date']
    auth=True
    if len(name)<2:
        auth=False
        messages.add_message(request,messages.ERROR,'Name must be at least 3 characters')
    if len(username)<2:
        auth=False
        messages.add_message(request,messages.ERROR,'Username must be at least 3 characters')
    if not REGEX.match(email):
        auth=False
        messages.add_message(request,messages.ERROR,'Invalid Email')
    if len(password)<8:
        auth=False
        messages.add_message(request,messages.ERROR,'Passwords must be at least 8 characters long')
    if password!=password_confirm:
        auth=False
        messages.add_message(request,messages.ERROR,'Passwords do not match')
    
    if auth == True:
        try:
            hashed_password=bcrypt.hashpw(password.encode('UTF-8'),bcrypt.gensalt())    
            user = User.objects.create(name=name, email=email, password=hashed_password, user_name=username, hired=date)
            request.session['user_id']=user.id
            request.session['user_name']=user.user_name
            return redirect('home:home')
        except:
             messages.add_message(request,messages.ERROR,'Email already exists')
             return redirect('user:home')

    else:
        return redirect('user:home')

def login(request):
    username=request.POST['html_username']
    server_password=request.POST['html_password']

    try:
        user = User.objects.get(user_name=username)
        if user.password == bcrypt.hashpw(server_password.encode('UTF-8'), user.password.encode('UTF-8')):

            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('home:home')
        else:
            messages.add_message(request,messages.ERROR,'Invalid login')
            return redirect('user:home')
                      
    except:
        messages.add_message(request,messages.ERROR,'Username does not exist')
        return redirect('user:home')

def logout(request):
    request.session.clear()
    return redirect('user:home')