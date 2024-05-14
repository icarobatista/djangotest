from django.shortcuts import render, redirect
from .  forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def homepage(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return redirect("login")

def register(request):
    #Valida formulário de registro e Sava Usuário
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerForm': form}
    return render(request, 'auth/register.html', context=context)

def login(request):
    #valida Formulário de Login
    form = LoginForm(request, request.POST)
    if form.is_valid:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Autentica Usuário e redireciona para dashboard
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")


    
    context = {'loginForm': form}
    return render(request, 'auth/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("")
    
@login_required
def dashboard(request): 
    return render(request, 'tasks/dashboard.html')
