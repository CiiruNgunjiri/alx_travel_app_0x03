from celery import shared_task
from django.core.mail import send_mail
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
@shared_task
def send_payment_confirmation_email(email, booking_reference):
    subject = "Booking Payment Confirmation"
    message = f"Your payment for booking {booking_reference} was successful."
    send_mail(subject, message, 'no-reply@yourdomain.com', [email])
