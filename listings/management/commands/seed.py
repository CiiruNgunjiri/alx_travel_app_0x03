from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
from django.contrib.auth.models import User
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def add_arguments(self, parser):
        parser.add_argument(
            '--listings', type=int, default=15,
            help='Number of listings to create'
        )

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(username='default_host')

        sample_listings = [
            {'title': 'Cozy Cottage', 'description': 'A cozy place in the woods.', 'price_per_night': 80.00, 'location': 'Forestville'},
            {'title': 'City Apartment', 'description': 'Modern apartment in the city center.', 'price_per_night': 120.00, 'location': 'Downtown'},
            {'title': 'Beach House', 'description': 'Sunny beachfront property.', 'price_per_night': 200.00, 'location': 'Seaside'}
        ]

        created_count = 0
        for item in sample_listings:
            try:
                obj, created = Listing.objects.get_or_create(
                    title=item['title'],
                    host=user,
                    defaults={
                        'description': item['description'],
                        'price_per_night': item['price_per_night'],
                        'location': item['location'],
                    }
                )
                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Listing '{obj.title}' created successfully"))
                else:
                    self.stdout.write(self.style.WARNING(f"Listing '{obj.title}' already exists - skipped"))
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(f"Could not create listing '{item['title']}': {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Unexpected error: {e}"))
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} listings"))
