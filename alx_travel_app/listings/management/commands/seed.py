from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
from django.contrib.auth.models import User
import random
from alx_travel_app.listings.serializers import ListingSerializer


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def add_arguments(self, parser):
        parser.add_argument(
        '--listings', type=int, default=15,
        help='Number of listings to create'
    )

    def handle(self, *args, **kwargs):
        # Create or get a default user to own listings
        user, created = User.objects.get_or_create(username='default_host')

        sample_listings = [
            {'title': 'Cozy Cottage', 'description': 'A cozy place in the woods.', 'price_per_night': 80.00, 'location': 'Forestville'},
            {'title': 'City Apartment', 'description': 'Modern apartment in the city center.', 'price_per_night': 120.00, 'location': 'Downtown'},
            {'title': 'Beach House', 'description': 'Sunny beachfront property.', 'price_per_night': 200.00, 'location': 'Seaside'}
            # Add more sample data as needed
        ]

        for item in sample_listings:
            Listing.objects.create(
                title=item['title'],
                description=item['description'],
                price_per_night=item['price_per_night'],
                host=user,
                location=item['location']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
