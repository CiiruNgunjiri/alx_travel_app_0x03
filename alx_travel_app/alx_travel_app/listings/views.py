from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.http import require_GET

def index(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})

# ******you could also use!******

# from django.http import HttpResponse

# def index(request):
#   return HttpResponse("Welcome to the Listings app!")

@require_GET
def custom_logout(request):
    logout(request)
    return redirect('home')
