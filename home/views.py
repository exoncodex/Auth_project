from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")  # Or redirect wherever you want

    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Log in successfully")
            return redirect("index")  # Redirect to index after login
        else:
            messages.error(request, "Wrong password or username")
            # Fall through and render login page again with message
        
    return render(request, "login.html")
def logout(request):
  auth_logout(request)
  return redirect("login")
  return render(request,"logout.html")
def index(request):
  if request.user.is_anonymous:
    return redirect("login")
  return render(request,"index.html")
  