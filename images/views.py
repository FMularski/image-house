from django.shortcuts import render


def sign_up(request):
    context = {}
    return render(request, 'images/sign_up.html', context)
