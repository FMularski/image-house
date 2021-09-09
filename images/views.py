from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import JsonResponse
from . import forms


def sign_in(request):
    form = forms.SignInForm()

    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.user_cache
            login(request, user)
            return redirect(reverse('home', ))

        messages.error(request, 'Invalid credentials.')

    context = {'form': form}
    return render(request, 'images/sign_in.html', context)


def sign_up(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User \'{form.cleaned_data.get("username")}\' has been signed up.')
            return redirect(reverse('sign_in', ))

    context = {'form': form}
    return render(request, 'images/sign_up.html', context)


@login_required(login_url='sign_in')
def home(request):
    return JsonResponse(data={'status': 200})


def sign_out(request):
    logout(request)
    return redirect(reverse('sign_in', ))
