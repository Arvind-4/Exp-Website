from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .forms import (
    SignInForm,
    SignUpForm,
)

User = get_user_model()

SESSION_EXPIRE_TIME = 604800

def signup_view(request: HttpRequest, *args, **kwargs):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password =  form.cleaned_data.get('password2')
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('sign-in')
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign-up.html', context)

def signin_view(request: HttpRequest, *args, **kwargs):
    form = SignInForm(request.POST or None)
    if form.is_valid():
        email   = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember_me = request.POST.get('remember_me') or None
        if remember_me is not None:
            request.session.set_expiry(SESSION_EXPIRE_TIME)
            print('You are Remembered!')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next') or None
            if next_url:
                return redirect(next_url)
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign-in.html', context)

@login_required
def signout_view(request:HttpRequest, *args, **kwargs):
    print(request.user.is_authenticated)
    logout(request)
    return redirect('/')