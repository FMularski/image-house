from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import JsonResponse
from . import forms, models


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
    images = models.Image.objects.select_related('user', 'category').all()
    most_viewed = images.order_by('-views').first()
    most_voted = images.order_by('-votes').first()
    most_recent = images.order_by('created_at').first()

    if request.GET.get('category'):
        images = images.filter(category__name=request.GET.get('category'))

    categories = models.Category.objects.all()

    context = {'images': images, 'most_viewed': most_viewed, 
                'most_voted': most_voted, 'most_recent': most_recent, 
                'categories': categories}
    return render(request, 'images/home.html', context)


@login_required(login_url='sign_in')
def my_images(request):
    my_images = models.Image.objects.select_related('user', 'category').filter(user=request.user)
    
    context = {'my_images': my_images}
    return render(request, 'images/my_images.html', context)


@login_required(login_url='sign_in')
def delete_img(request, pk):
    models.Image.objects.get(pk=pk).delete()
    messages.success(request, 'Image has been deleted.')
    
    return redirect(reverse('my_images', ))


@login_required(login_url='sign_in')
def image(request, pk):
    image = models.Image.objects.select_related('user', 'category').get(pk=pk)
    image.views += 1
    image.save()

    context = {'image': image}
    return render(request, 'images/image.html', context)


@login_required(login_url='sign_in')
def vote(request, pk, vote):
    image = models.Image.objects.get(pk=pk)
    image.votes += vote if vote else -1
    image.save()
    
    return redirect(reverse('image', kwargs={'pk': pk}))


@login_required(login_url='sign_in')
def add_image(request):
    form = forms.ImageForm()

    if request.method == 'POST':
        print(request.POST)
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()

            messages.success(request, 'Image has been added.')
            return redirect(reverse('my_images', ))

    context = {'form': form}
    return render(request, 'images/add.html', context)


def sign_out(request):
    logout(request)
    return redirect(reverse('sign_in', ))
