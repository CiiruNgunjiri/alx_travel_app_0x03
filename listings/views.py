from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})

# ******you could also use!******

# from django.http import HttpResponse

# def index(request):
#   return HttpResponse("Welcome to the Listings app!")