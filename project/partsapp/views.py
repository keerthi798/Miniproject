from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount,SocialApp
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import CustomUser  # Ensure the correct import path for CustomUser model

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if the email already exists in the database
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email address is already in use.'})

        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Create a new user object
        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        # Store user ID in the session
       
        # Redirect to the dashboard after successful registration
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use 'auth_login' to avoid conflicts
              # Store user ID in the session
            return redirect('dashboard')
        else:
            # Check if username exists in the database
            if not CustomUser.objects.filter(username=username).exists():
                error_message = 'Wrong username'
            else:
                error_message = 'Wrong password'

            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logout_confirm(request):
    if request.user.is_authenticated:
          # Remove your custom session data
        
        # Clear any Google-related session data if you have stored it
       
        logout(request)
    return render(request, 'logout_confirm.html')

def dashboard(request):
    # Use session data to retrieve the user object
  return redirect('index')
def booking(request):
    # Use session data to retrieve the user object
   return render(request, 'booking.html')
