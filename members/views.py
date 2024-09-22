from django.shortcuts import render, redirect  
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in")
                return redirect('/')
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.success(request, 'You must pass the reCHAPTCHA test')
                    continue
                messages.error(request, error)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, 'You must pass the reCHAPTCHA test')
                    continue
                messages.error(request, error)
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
