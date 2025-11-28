from socials.facebook_service import FacebookFeedService
from socials.models import SocialPost, SocialMediaChannel
from django.conf import settings
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import requests
import re


class SocialFeedSync:
    """
    A utility class to sync social media feeds from various platforms
    """

    @staticmethod
    def sync_facebook_page(page_url, limit=10):
        """
        Sync posts from a Facebook page
        """
        # Extract page ID or username from URL
        match = re.search(r'facebook\.com/([^/?]+)', page_url)
        if not match:
            raise ValueError("Invalid Facebook page URL")

        page_identifier = match.group(1)

        service = FacebookFeedService()
        return service.sync_page_posts(page_identifier, limit)

    @staticmethod
    def sync_youtube_channel(channel_url, limit=10):
        """
        Sync videos from a YouTube channel
        """
        # Extract channel ID or username
        api_key = getattr(settings, 'YOUTUBE_API_KEY', None)
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY not configured in settings")

        # Extract channel ID from URL
        channel_id = None
        if 'channel/' in channel_url:
            # e.g. https://www.youtube.com/channel/UC...
            channel_id = channel_url.split('channel/')[1].split('/')[0]
        elif 'user/' in channel_url:
            # e.g. https://www.youtube.com/user/username
            username = channel_url.split('user/')[1].split('/')[0]
            # Note: Need to get channel ID from username via API
            channel_id = SocialFeedSync._get_channel_id_from_username(username, api_key)
        elif 'c/' in channel_url:
            # e.g. https://www.youtube.com/c/channelname
            channel_name = channel_url.split('c/')[1].split('/')[0]
            # Note: Need to get channel ID from custom URL via API
            channel_id = SocialFeedSync._get_channel_id_from_custom_url(channel_name, api_key)

        if not channel_id:
            raise ValueError("Could not extract YouTube channel ID from URL")

        # Get uploads playlist ID
        uploads_playlist_id = f"UU{channel_id[2:]}"  # Convert channel ID to uploads playlist ID

        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            'part': 'snippet',
            'playlistId': uploads_playlist_id,
            'maxResults': limit,
            'key': api_key,
            'order': 'date'  # Order by date to get newest first
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            created_count = 0
            for item in data.get('items', []):
                snippet = item.get('snippet', {})
                video_id = snippet.get('resourceId', {}).get('videoId')
                title = snippet.get('title', '')
                description = snippet.get('description', '')
                published_at_str = snippet.get('publishedAt', '')
                channel_title = snippet.get('channelTitle', '')

                if video_id:
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    published_at = parse_datetime(published_at_str) if published_at_str else None

                    # Create or update SocialPost
                    existing_post, created = SocialPost.objects.get_or_create(
                        url=video_url,
                        defaults={
                            'platform': 'YOUTUBE',
                            'title': title[:500],
                            'caption': description[:500],
                            'author': channel_title[:200],
                            'published_date': published_at,
                            'is_active': True
                        }
                    )

                    if created:
                        created_count += 1

            return created_count
        except Exception as e:
            print(f"Error syncing YouTube channel: {e}")
            return 0

    @staticmethod
    def sync_tiktok_channel(channel_url, limit=10):
        """
        Sync videos from a TikTok user profile
        Note: This is more complex and may have limitations
        """
        # Extract username from TikTok URL
        match = re.search(r'tiktok\.com/@([^/?]+)', channel_url)
        if not match:
            raise ValueError("Invalid TikTok profile URL")

        username = match.group(1)

        # Unfortunately, TikTok doesn't have a public API for fetching user posts
        # This is a limitation, so we would need to use a different approach
        # such as web scraping (which may violate ToS) or a third-party service
        # For now, this is a framework that would need to be implemented carefully

        print(f"TikTok sync for @{username} requires special implementation")
        print("TikTok doesn't provide a public API for fetching user posts")
        print("This would require a different approach or third-party service")

        # Placeholder - would need to implement with proper service
        return 0

    @staticmethod
    def _get_channel_id_from_username(username, api_key):
        """
        Get YouTube channel ID from username
        """
        url = "https://www.googleapis.com/youtube/v3/channels"
        params = {
            'part': 'id',
            'forUsername': username,
            'key': api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            items = data.get('items', [])
            if items:
                return items[0].get('id')
        except Exception as e:
            print(f"Error getting channel ID for username {username}: {e}")

        return None

    @staticmethod
    def _get_channel_id_from_custom_url(custom_url, api_key):
        """
        Get YouTube channel ID from custom URL
        """
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': custom_url,
            'type': 'channel',
            'maxResults': 1,
            'key': api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            items = data.get('items', [])
            if items:
                return items[0]['snippet']['channelId']
        except Exception as e:
            print(f"Error getting channel ID for custom URL {custom_url}: {e}")

        return None

    @staticmethod
    def sync_all_active_channels():
        """
        Sync all active social media channels
        """
        channels = SocialMediaChannel.objects.filter(is_active=True)
        results = {}

        for channel in channels:
            try:
                if channel.platform == 'YOUTUBE':
                    count = SocialFeedSync.sync_youtube_channel(
                        channel.channel_url,
                        limit=10  # Get last 10 videos
                    )
                    results[f"youtube_{channel.channel_identifier}"] = count
                elif channel.platform == 'FACEBOOK':
                    count = SocialFeedSync.sync_facebook_page(
                        channel.channel_url,
                        limit=10
                    )
                    results[f"facebook_{channel.channel_identifier}"] = count
                elif channel.platform == 'TIKTOK':
                    # TikTok sync is more complex and may require special handling
                    count = SocialFeedSync.sync_tiktok_channel(
                        channel.channel_url,
                        limit=10
                    )
                    results[f"tiktok_{channel.channel_identifier}"] = count
                elif channel.platform == 'INSTAGRAM':
                    # Instagram would require Instagram Business API or other approach
                    results[f"instagram_{channel.channel_identifier}"] = 0
                    print(f"Instagram sync not implemented for {channel.channel_identifier}")

                # Update last sync timestamp
                channel.last_sync = timezone.now()
                channel.save()

            except Exception as e:
                print(f"Error syncing {channel.platform} channel {channel.channel_identifier}: {e}")
                results[f"{channel.platform.lower()}_{channel.channel_identifier}_error"] = str(e)

        return results