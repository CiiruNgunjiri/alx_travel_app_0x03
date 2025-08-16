from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from listings.views import ListingViewSet, BookingViewSet
from .views import initiate_payment, verify_payment, create_booking

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    # Example endpoint, you can replace or extend this later
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('initiate_payment/', initiate_payment, name='initiate_payment'),
    path('verify_payment/', verify_payment, name='verify_payment'),
    path('create_booking/', create_booking, name='create_booking'),
]
