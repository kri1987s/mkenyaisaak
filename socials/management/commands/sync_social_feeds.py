from django.core.management.base import BaseCommand
from socials.feed_sync import SocialFeedSync


class Command(BaseCommand):
    help = 'Sync all active social media channels'

    def add_arguments(self, parser):
        parser.add_argument(
            '--platform',
            type=str,
            help='Sync specific platform (youtube, facebook, tiktok, instagram)',
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=10,
            help='Number of posts to fetch per channel (default: 10)',
        )

    def handle(self, *args, **options):
        platform = options.get('platform')
        limit = options.get('limit', 10)
        
        self.stdout.write(
            self.style.SUCCESS(f'Starting sync for all active channels (limit: {limit})')
        )
        
        try:
            results = SocialFeedSync.sync_all_active_channels()
            
            for channel, count in results.items():
                if '_error' in channel:
                    self.stdout.write(
                        self.style.ERROR(f'Error syncing {channel}: {count}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'Synced {count} items from {channel}')
                    )
            
            self.stdout.write(
                self.style.SUCCESS('Sync completed successfully')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during sync: {str(e)}')
            )