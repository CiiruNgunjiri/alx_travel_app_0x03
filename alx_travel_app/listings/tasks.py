from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = 'Booking Confirmation'
    message = f"Thank you for your booking!\n\nDetails:\n{booking_details}"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [to_email])

@shared_task
def send_payment_confirmation_email(email, booking_reference):
    subject = "Booking Payment Confirmation"
    message = f"Your payment for booking {booking_reference} was successful."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)