from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # Passa apenas os dados do POST
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main_page')  # Redirecionar para a página inicial
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def main_page(request):
    return render(request, 'accounts/main.html')
