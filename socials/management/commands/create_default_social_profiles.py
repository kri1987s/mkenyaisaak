from django.core.management.base import BaseCommand
from socials.models import SocialProfile

class Command(BaseCommand):
    help = 'Creates default social media profiles'

    def handle(self, *args, **options):
        profiles_data = [
            {
                'platform': 'TIKTOK',
                'profile_url': 'https://www.tiktok.com/@mkenya7million',
                'display_name': '@mkenya7million'
            },
            {
                'platform': 'INSTAGRAM',
                'profile_url': 'https://www.instagram.com/mkenyaisaak/',
                'display_name': '@mkenyaisaak'
            },
            {
                'platform': 'YOUTUBE',
                'profile_url': 'https://www.youtube.com/@mkenyaisaak',
                'display_name': 'Mkenya Isaak 7Million'
            },
            {
                'platform': 'FACEBOOK',
                'profile_url': 'https://web.facebook.com/seven7miIlion/',
                'display_name': 'Mkenya Isaak 7Million'
            }
        ]

        for profile_data in profiles_data:
            profile, created = SocialProfile.objects.get_or_create(
                platform=profile_data['platform'],
                defaults={
                    'profile_url': profile_data['profile_url'],
                    'display_name': profile_data['display_name'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created {profile.get_platform_display()} profile')
                )
            else:
                self.stdout.write(
                    f'Found existing {profile.get_platform_display()} profile'
                )