from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(email, booking_reference):
    subject = "Booking Payment Confirmation"
    message = f"Your payment for booking {booking_reference} was successful."
    send_mail(subject, message, 'no-reply@yourdomain.com', [email])
