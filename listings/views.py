from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.http import require_GET

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from listings.models import Listing, Booking
from listings.serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    list:
    Retrieve all listings.

    retrieve:
    Get a single listing by ID.

    create:
    Create a new listing.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    @swagger_auto_schema(operation_summary="List all listings")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @swagger_auto_schema(
        operation_description="Create a new booking",
        responses={201: BookingSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
