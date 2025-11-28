from django.core.management.base import BaseCommand
from socials.feed_sync import SocialFeedSync


class Command(BaseCommand):
    help = 'Sync YouTube channel feeds'

    def add_arguments(self, parser):
        parser.add_argument('--channel-url', type=str, help='YouTube channel URL to sync')
        parser.add_argument('--limit', type=int, default=10, help='Number of videos to fetch (default: 10)')

    def handle(self, *args, **options):
        channel_url = options['channel_url']
        limit = options['limit']
        
        if not channel_url:
            self.stdout.write(
                self.style.ERROR('Please provide a YouTube channel URL using --channel-url')
            )
            return
        
        try:
            created_count = SocialFeedSync.sync_youtube_channel(channel_url, limit)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully synced {created_count} new YouTube videos from {channel_url}'
                )
            )
        except ValueError as e:
            self.stdout.write(
                self.style.ERROR(str(e))
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error syncing YouTube channel: {str(e)}')
            )