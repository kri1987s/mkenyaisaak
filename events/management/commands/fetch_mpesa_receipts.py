from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Booking
from events.utils import check_mpesa_transaction_status
from datetime import timedelta


class Command(BaseCommand):
    help = 'Fetch M-Pesa receipt codes for bookings that are missing them'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Fetch receipt codes for all bookings without M-Pesa receipt numbers',
        )
        parser.add_argument(
            '--paid-only',
            action='store_true',
            help='Only fetch receipt codes for bookings with PAID status',
        )
        parser.add_argument(
            '--days',
            type=int,
            default=7,
            help='Number of days to look back for bookings (default: 7)',
        )

    def handle(self, *args, **options):
        # Determine which bookings to check
        if options['all']:
            # All bookings without M-Pesa receipt number
            bookings = Booking.objects.filter(
                mpesa_receipt_number__isnull=True,
                payment_reference__isnull=False
            ).order_by('-created_at')
        elif options['paid_only']:
            # Only paid bookings without M-Pesa receipt number
            bookings = Booking.objects.filter(
                payment_status='PAID',
                mpesa_receipt_number__isnull=True,
                payment_reference__isnull=False
            ).order_by('-created_at')
        else:
            # Default: Paid bookings without M-Pesa receipt in the last X days
            days_ago = timezone.now() - timedelta(days=options['days'])
            bookings = Booking.objects.filter(
                payment_status='PAID',
                mpesa_receipt_number__isnull=True,
                payment_reference__isnull=False,
                created_at__gte=days_ago
            ).order_by('-created_at')

        self.stdout.write(
            self.style.WARNING(f'Found {bookings.count()} bookings to check')
        )

        updated_count = 0
        failed_count = 0

        for booking in bookings:
            self.stdout.write(f'Checking booking {booking.id} with reference {booking.payment_reference}...')
            
            try:
                success = check_mpesa_transaction_status(booking)
                if success:
                    self.stdout.write(
                        self.style.SUCCESS(f'Updated booking {booking.id} with M-Pesa receipt: {booking.mpesa_receipt_number}')
                    )
                    updated_count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(f'No receipt found yet for booking {booking.id}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error checking booking {booking.id}: {str(e)}')
                )
                failed_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Completed! Updated {updated_count} bookings, {failed_count} failed, '
                f'{bookings.count() - updated_count - failed_count} still pending'
            )
        )