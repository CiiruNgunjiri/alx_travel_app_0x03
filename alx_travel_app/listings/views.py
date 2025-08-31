import uuid
import json
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, filters

from listings.models import Listing, Booking, Payment
from listings.serializers import ListingSerializer, BookingSerializer


def create_booking(request):
    if request.method == 'POST':
        # Extract booking data from request.POST or request.data
        booking_data = {
            'user': request.user,
            # Include other booking data fields here as needed
        }
        # Create booking object (assuming you have a Booking model)
        booking = Booking.objects.create(
            user=request.user,
            # Assign other fields from booking_data if any
        )

        # Prepare data to initiate payment
        payment_data = {
            'booking_reference': str(booking.id),  # Unique reference, e.g. booking id
            'amount': booking.total_price,          # Total price for payment
            'email': request.user.email,
            'first_name': getattr(request.user, 'first_name', ''),
            'last_name': getattr(request.user, 'last_name', '')
        }

        # Initiate payment by posting data to payment API endpoint
        response = requests.post(
            request.build_absolute_uri(reverse('initiate_payment')),
            json=payment_data
        )

        if response.status_code == 200:
            response_data = response.json()
            payment_url = response_data.get('payment_url')
            # Redirect the user to Chapa payment checkout page
            return redirect(payment_url)
        else:
            # Handle error (render error page or message)
            return render(request, 'error.html', {'message': 'Payment initiation failed'})

    # For GET or other methods, render booking form page
    return render(request, 'booking_form.html')


def index(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})


@require_GET
def custom_logout(request):
    logout(request)
    return redirect('home')


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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price_per_night', 'created_at']

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


@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        booking_ref = data.get('booking_reference')
        amount = data.get('amount')
        email = data.get('email')
        first_name = data.get('first_name', 'Guest')
        last_name = data.get('last_name', '')

        # Generate a unique transaction reference (tx_ref) using UUID
        tx_ref = str(uuid.uuid4())

        # Optional: Retrieve booking for verification, remove this if not needed
        try:
            booking = Booking.objects.get(id=booking_ref)
        except Booking.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)

        # Create or update Payment object
        payment, created = Payment.objects.get_or_create(
            booking_reference=booking_ref,
            defaults={'amount': amount, 'status': 'Pending'}
        )

        payment.amount = amount
        payment.status = 'Pending'
        payment.save()

        # Prepare payload for Chapa API
        payload = {
            "amount": amount,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "tx_ref": tx_ref,
            "callback_url": "http://localhost.com/api/verify_payment/",  # Change to your actual callback URL
            "currency": "ETB"
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        # Initiate payment with Chapa
        response = requests.post(settings.CHAPA_API_URL, json=payload, headers=headers)
        chapa_response = response.json()

        if response.status_code == 200 and chapa_response.get('status') == 'success':
            payment.transaction_id = chapa_response['data']['id']
            payment.save()
            return JsonResponse({
                "payment_url": chapa_response['data']['checkout_url'],
                "message": "Payment initiated"
            })
        else:
            return JsonResponse({"error": "Payment initiation failed"}, status=400)


@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        booking_ref = data.get('booking_reference')

        try:
            payment = Payment.objects.get(booking_reference=booking_ref)
        except Payment.DoesNotExist:
            return JsonResponse({"error": "Payment not found"}, status=404)

        verify_url = f"{settings.CHAPA_VERIFY_URL}{payment.transaction_id}"

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        }

        response = requests.get(verify_url, headers=headers)
        chapa_response = response.json()

        if response.status_code == 200 and chapa_response.get('status') == 'success':
            if chapa_response['data']['status'] == 'success':
                payment.status = 'Completed'
            else:
                payment.status = 'Failed'
            payment.save()
            return JsonResponse({"status": payment.status})
        else:
            return JsonResponse({"error": "Verification failed"}, status=400)
import uuid
import json
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, filters

from listings.models import Listing, Booking, Payment
from listings.serializers import ListingSerializer, BookingSerializer

from .tasks import send_booking_confirmation_email

def create_booking(request):
    if request.method == 'POST':
        # Extract booking data from request.POST or request.data
        booking_data = {
            'user': request.user,
            # Include other booking data fields here as needed
        }
        # Create booking object (assuming you have a Booking model)
        booking = Booking.objects.create(
            user=request.user,
            # Assign other fields from booking_data if any
        )

        # Prepare data to initiate payment
        payment_data = {
            'booking_reference': str(booking.id),  # Unique reference, e.g. booking id
            'amount': booking.total_price,          # Total price for payment
            'email': request.user.email,
            'first_name': getattr(request.user, 'first_name', ''),
            'last_name': getattr(request.user, 'last_name', '')
        }

        # Initiate payment by posting data to payment API endpoint
        response = requests.post(
            request.build_absolute_uri(reverse('initiate_payment')),
            json=payment_data
        )

        if response.status_code == 200:
            response_data = response.json()
            payment_url = response_data.get('payment_url')
            # Redirect the user to Chapa payment checkout page
            return redirect(payment_url)
        else:
            # Handle error (render error page or message)
            return render(request, 'error.html', {'message': 'Payment initiation failed'})

    # For GET or other methods, render booking form page
    return render(request, 'booking_form.html')


def index(request):
    return JsonResponse({"message": "Welcome to ALX Travel Listings API"})


@require_GET
def custom_logout(request):
    logout(request)
    return redirect('home')


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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price_per_night', 'created_at']

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

    def perform_create(self, serializer):
        booking = serializer.save()

        # Prepare booking details string
        booking_details = f"Booking ID: {booking.id}\nDate: {booking.date}\nDetails: {booking.other_fields}"

        # Trigger async email sending
        send_booking_confirmation_email.delay(booking.user.email, booking_details)

@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        booking_ref = data.get('booking_reference')
        amount = data.get('amount')
        email = data.get('email')
        first_name = data.get('first_name', 'Guest')
        last_name = data.get('last_name', '')

        # Generate a unique transaction reference (tx_ref) using UUID
        tx_ref = str(uuid.uuid4())

        # Optional: Retrieve booking for verification, remove this if not needed
        try:
            booking = Booking.objects.get(id=booking_ref)
        except Booking.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)

        # Create or update Payment object
        payment, created = Payment.objects.get_or_create(
            booking_reference=booking_ref,
            defaults={'amount': amount, 'status': 'Pending'}
        )

        payment.amount = amount
        payment.status = 'Pending'
        payment.save()

        # Prepare payload for Chapa API
        payload = {
            "amount": amount,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "tx_ref": tx_ref,
            "callback_url": "http://localhost.com/api/verify_payment/",  # Change to your actual callback URL
            "currency": "ETB"
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        # Initiate payment with Chapa
        response = requests.post(settings.CHAPA_API_URL, json=payload, headers=headers)
        chapa_response = response.json()

        if response.status_code == 200 and chapa_response.get('status') == 'success':
            payment.transaction_id = chapa_response['data']['id']
            payment.save()
            return JsonResponse({
                "payment_url": chapa_response['data']['checkout_url'],
                "message": "Payment initiated"
            })
        else:
            return JsonResponse({"error": "Payment initiation failed"}, status=400)


@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        booking_ref = data.get('booking_reference')

        try:
            payment = Payment.objects.get(booking_reference=booking_ref)
        except Payment.DoesNotExist:
            return JsonResponse({"error": "Payment not found"}, status=404)

        verify_url = f"{settings.CHAPA_VERIFY_URL}{payment.transaction_id}"

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        }

        response = requests.get(verify_url, headers=headers)
        chapa_response = response.json()

        if response.status_code == 200 and chapa_response.get('status') == 'success':
            if chapa_response['data']['status'] == 'success':
                payment.status = 'Completed'
            else:
                payment.status = 'Failed'
            payment.save()
            return JsonResponse({"status": payment.status})
        else:
            return JsonResponse({"error": "Verification failed"}, status=400)
