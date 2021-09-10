from django.shortcuts import redirect, reverse


class SuperMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):

        if (request.user.is_authenticated and request.path in ['/sign_in/', '/sign_up/']):
            return redirect(reverse('home', ))

        response = self.get_response(request)

        return response