from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm
from django.contrib.auth import login as login_func, logout as logout_func
from django.contrib.auth.models import User
from .models import Profile

def login(request):
    
    form = LoginForm(request)

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            login_func(request, form.get_user())
            return redirect('main')

    context = {'form': form}

    return render(request, 'users/login.html', context)

def logout_view(request):
    logout_func(request)
    return redirect('main')


def reg_form(request):
    form = RegForm()
    
    if request.method == 'POST':
        # редиректим на главную, если авторизован
        if request.user.is_authenticated:
            return redirect('/')
    
        form = RegForm(request.POST)
        
        if form.is_valid():
            # создаем пользователя
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password_1']
            )
            Profile.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name', ''),
                last_name=form.cleaned_data.get('last_name', '')
            )
            
            # авторизуем после регистрации
            login_func(request, user)
            
            return redirect('/')  # Или на страницу профиля: redirect('profile')
    
    context = {'form': form}
    return render(request, 'users/reg_form.html', context)