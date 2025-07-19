from rest_framework import serializers
from alx_travel_app.listings.models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'host', 'location', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'listing', 'start_date', 'end_date', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'listing',
            'rating',
            'comment',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']