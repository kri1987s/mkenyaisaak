import re
from urllib.parse import urlparse, parse_qs
import requests
from django.conf import settings


def extract_video_id_youtube(url):
    """Extract YouTube video ID from different URL formats"""
    # Various YouTube URL patterns
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]*)',
        r'(?:embed\/|v\/|watch\?v=|watch\?.+&v=)([^"&?\/\s]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            # Clean the ID in case there are additional parameters
            return video_id.split('&')[0].split('?')[0]
    
    return None


def extract_video_id_tiktok(url):
    """Extract TikTok video ID from URL"""
    # TikTok patterns - looking for the video ID in the URL
    patterns = [
        r'/video/(\d+)',
        r'/t/(\w+)',
        r'/(\d{18,19})',  # direct video ID in URL
        r'videoId=(\d+)',  # videoId parameter
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    # If we can't extract the ID, return None
    return None


def extract_post_id_instagram(url):
    """Extract Instagram post ID from URL"""
    patterns = [
        r'/p/([A-Za-z0-9_-]+)',
        r'/reel/([A-Za-z0-9_-]+)',
        r'/tv/([A-Za-z0-9_-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def extract_post_id_facebook(url):
    """Extract Facebook post ID from URL"""
    # Facebook URLs are more complex, we'll get the main components
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    
    # Look for post specific elements in the URL path
    for i, part in enumerate(path_parts):
        if part == 'posts' and i + 1 < len(path_parts):
            return path_parts[i + 1]
        elif part == 'video' and i + 1 < len(path_parts):
            return path_parts[i + 1]
    
    return None


def get_youtube_video_details(video_id):
    """Fetch video details from YouTube API (requires API key)"""
    api_key = getattr(settings, 'YOUTUBE_API_KEY', None)
    if not api_key:
        return None
    
    url = f"https://www.googleapis.com/youtube/v3/videos"
    params = {
        'part': 'snippet,statistics',
        'id': video_id,
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('items'):
            item = data['items'][0]
            snippet = item.get('snippet', {})
            stats = item.get('statistics', {})
            
            return {
                'title': snippet.get('title', ''),
                'description': snippet.get('description', ''),
                'channel': snippet.get('channelTitle', ''),
                'published_at': snippet.get('publishedAt', ''),
                'like_count': stats.get('likeCount', 0),
                'view_count': stats.get('viewCount', 0),
                'comment_count': stats.get('commentCount', 0),
            }
    except Exception as e:
        print(f"Error fetching YouTube video details: {e}")
    
    return None


def generate_youtube_embed(url):
    """Generate YouTube embed HTML from URL with responsive aspect ratio"""
    video_id = extract_video_id_youtube(url)
    if video_id:
        # YouTube has responsive embed options
        return f'<div class="ratio ratio-16x9"><iframe src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe></div>'
    return None


def generate_tiktok_embed(url):
    """Generate TikTok embed HTML from URL"""
    video_id = extract_video_id_tiktok(url)
    if video_id:
        # For TikTok, we'll provide a responsive container
        return f'<div class="tiktok-embed-container" style="position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;"><blockquote class="tiktok-embed" cite="{url}" data-video-id="{video_id}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;"> <section> <a target="_blank" href="{url}"></a> </section> </blockquote></div><script async src="https://www.tiktok.com/embed.js"></script>'
    return None


def generate_instagram_embed(url):
    """Generate Instagram embed HTML from URL with responsive aspect ratio"""
    post_id = extract_post_id_instagram(url)
    if post_id:
        # Instagram has responsive embed patterns
        return f'<div class="ratio ratio-4x5"><blockquote class="instagram-media" data-instgrm-permalink="{url}" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 0 auto; max-width:400px; padding:0; width:100%;"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding-top:100%;"><a href="{url}" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">Check out this post on Instagram</a></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="{url}" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">{url}</a></p> <p style=" margin:0 0 5px 0; padding:2px 0 0 0; font-family:Arial,sans-serif; font-size:11px; font-style:normal; font-weight:normal; line-height:11px; text-align:center; color:#c9c8cd;"> A post shared by <a href="https://www.instagram.com/_u/" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:11px; font-style:normal; font-weight:normal; line-height:11px; text-align:center;" target="_blank">Instagram</a></p></div></blockquote></div><script async defer src="//www.instagram.com/embed.js"></script>'
    return None


def generate_facebook_embed(url):
    """Generate Facebook embed HTML from URL"""
    # Facebook embeds are handled via their embedded post API
    return f'<div class="fb-post" data-href="{url}" data-width="500" data-show-text="true" style="margin: 0 auto;"><blockquote cite="{url}" class="fb-xfbml-parse-ignore" style="background: #fff; border: 1px solid #ddd; border-radius: 2px; padding: 10px;"><a href="{url}">Post</a></blockquote></div>'


def generate_embed_code(platform, url):
    """Generate embed code based on the platform and URL"""
    platform = platform.upper()
    
    if platform == 'YOUTUBE':
        return generate_youtube_embed(url)
    elif platform == 'TIKTOK':
        return generate_tiktok_embed(url)
    elif platform == 'INSTAGRAM':
        return generate_instagram_embed(url)
    elif platform == 'FACEBOOK':
        return generate_facebook_embed(url)
    else:
        return None