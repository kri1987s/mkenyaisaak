from django.core.management.base import BaseCommand
from socials.models import SocialPost


class Command(BaseCommand):
    help = 'Fetch and update video details for existing YouTube posts'

    def handle(self, *args, **options):
        # Get all YouTube posts that don't have titles yet
        youtube_posts = SocialPost.objects.filter(platform='YOUTUBE', title__isnull=True)
        youtube_posts = youtube_posts | SocialPost.objects.filter(platform='YOUTUBE', title='')
        
        updated_count = 0
        for post in youtube_posts:
            old_title = post.title
            post.fetch_youtube_details()
            post.save()
            
            if post.title and post.title != old_title:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated: {post.title}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Updated video details for {updated_count} YouTube posts')
        )