from django.core.management.base import BaseCommand
from socials.facebook_service import fetch_facebook_page_feed


class Command(BaseCommand):
    help = 'Fetch and sync Facebook page feed to SocialPost model'

    def add_arguments(self, parser):
        parser.add_argument('--page-url', type=str, help='Facebook page URL to fetch posts from')
        parser.add_argument('--limit', type=int, default=10, help='Number of posts to fetch (default: 10)')

    def handle(self, *args, **options):
        page_url = options['page_url']
        limit = options['limit']
        
        if not page_url:
            self.stdout.write(
                self.style.ERROR('Please provide a Facebook page URL using --page-url')
            )
            return
        
        try:
            created_count = fetch_facebook_page_feed(page_url, limit)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully synced {created_count} new Facebook posts from {page_url}'
                )
            )
        except ValueError as e:
            self.stdout.write(
                self.style.ERROR(str(e))
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error syncing Facebook posts: {str(e)}')
            )