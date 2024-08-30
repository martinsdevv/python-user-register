from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def main_page(request):
    return render(request, 'accounts/main.html')

def reset_password_basic(request):
    # Lógica da view para resetar a senha
    return render(request, 'accounts/reset_password.html')