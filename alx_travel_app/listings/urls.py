from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from listings.views import ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    # Example endpoint, you can replace or extend this later
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
