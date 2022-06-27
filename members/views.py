from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import NewUserForm, Login




def login_user(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.username, password=form.password)
            if user is not None:
                 login(request, user)
                 messages.success(request, "Login successful." )
                 return redirect("home")
            else:
                messages.error(request, "Error, try again")
    else:
        form = Login()
        return render (request, "login.html", {"form":form})

def logout(request):
    logout(request)
    messages.success(request, "Sucesfully logout" )
    return redirect('home')    

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "registration/signup.html", {"register_form":form})