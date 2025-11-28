import requests
import json
from django.conf import settings
from .models import SocialPost


class FacebookFeedService:
    """
    Service to fetch Facebook page posts and convert them to SocialPost objects
    """
    
    def __init__(self, access_token=None):
        self.access_token = access_token or getattr(settings, 'FACEBOOK_ACCESS_TOKEN', None)
        self.base_url = 'https://graph.facebook.com/v18.0'
        
    def get_page_posts(self, page_id_or_username, limit=10):
        """
        Fetch posts from a Facebook page
        """
        if not self.access_token:
            raise ValueError("Facebook access token is required")
        
        url = f"{self.base_url}/{page_id_or_username}/posts"
        params = {
            'access_token': self.access_token,
            'fields': 'id,message,created_time,attachments{type,url,title,description},permalink_url',
            'limit': limit
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            posts = []
            for item in data.get('data', []):
                post_data = self._process_facebook_post(item)
                if post_data:
                    posts.append(post_data)
            
            return posts
        except requests.RequestException as e:
            print(f"Error fetching Facebook posts: {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error parsing Facebook response: {e}")
            return []

    def _process_facebook_post(self, post_data):
        """
        Process a single Facebook post and extract relevant information
        """
        post_id = post_data.get('id', '').split('_')[-1]  # Extract just the post ID
        message = post_data.get('message', '')
        created_time = post_data.get('created_time', '')
        permalink_url = post_data.get('permalink_url', '')
        
        # Look for video or link attachments
        attachment = None
        attachments = post_data.get('attachments', {}).get('data', [])
        
        if attachments:
            for attach in attachments:
                if attach.get('type') in ['video_inline', 'video', 'photo', 'link']:
                    attachment = attach
                    break
        
        # Determine if this post has content we can work with
        if not permalink_url:
            return None
            
        # Create processed post data
        processed = {
            'platform': 'FACEBOOK',
            'url': permalink_url,
            'caption': message,
            'created_time': created_time,
        }
        
        return processed

    def sync_page_posts(self, page_id_or_username, limit=10):
        """
        Sync Facebook page posts to SocialPost model
        """
        posts = self.get_page_posts(page_id_or_username, limit)
        
        created_count = 0
        for post_data in posts:
            # Check if post already exists (based on URL)
            existing_post, created = SocialPost.objects.get_or_create(
                url=post_data['url'],
                defaults={
                    'platform': post_data['platform'],
                    'caption': post_data['caption'],
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                
        return created_count


def fetch_facebook_page_feed(page_url, limit=10):
    """
    Function to fetch Facebook page feed and create SocialPost entries
    """
    # Extract page ID or username from URL
    import re
    match = re.search(r'facebook\.com/([^/?]+)', page_url)
    if not match:
        raise ValueError("Invalid Facebook page URL")
    
    page_identifier = match.group(1)
    
    service = FacebookFeedService()
    return service.sync_page_posts(page_identifier, limit)