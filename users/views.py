from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def welcome(request):
    return render(request, "users/welcome.html")

def register_page(request):
    if request.user.is_authenticated:
        return redirect('users:welcome') #redirect if login
    
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    
    return render(request, "users/register.html", {"form":form})

def login_page(request):

    #to redirect user to the last page after login
    next_url = request.GET.get('next', 'tasks:home') #2nd arg is fallback if their is no next

    if request.user.is_authenticated:
        return redirect('tasks:home') #redirect if login
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() #retrive aunthenticated user
            login(request, user) #login the user
            return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form":form, 'next':next_url})

def logout_view(request):
    logout(request)
    return redirect('users:login')
