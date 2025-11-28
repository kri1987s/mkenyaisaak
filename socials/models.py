from django.db import models
from .utils import generate_embed_code, get_youtube_video_details


class SocialMediaChannel(models.Model):
    """Model to store social media channels for automated feed fetching"""
    PLATFORM_CHOICES = [
        ('TIKTOK', 'TikTok'),
        ('YOUTUBE', 'YouTube'),
        ('FACEBOOK', 'Facebook'),  # Already implemented
        ('INSTAGRAM', 'Instagram'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    channel_url = models.URLField(help_text="URL to the social media channel/profile")
    channel_identifier = models.CharField(
        max_length=200,
        help_text="Unique identifier for the channel (e.g., username, ID)",
        unique=True
    )
    display_name = models.CharField(max_length=200, blank=True, help_text="Display name for the channel")
    is_active = models.BooleanField(default=True, help_text="Enable automatic feed fetching for this channel")
    last_sync = models.DateTimeField(null=True, blank=True, help_text="Last time the feed was synced")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Media Channel"
        verbose_name_plural = "Social Media Channels"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_platform_display()} - {self.display_name or self.channel_identifier}"


class SocialProfile(models.Model):
    """Model to store social media profile links for the website"""
    PLATFORM_CHOICES = [
        ('TIKTOK', 'TikTok'),
        ('INSTAGRAM', 'Instagram'),
        ('YOUTUBE', 'YouTube'),
        ('FACEBOOK', 'Facebook'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    profile_url = models.URLField(help_text="URL to the social media profile")
    display_name = models.CharField(max_length=100, blank=True, help_text="Display name for the profile (optional)")
    is_active = models.BooleanField(default=True, help_text="Show in footer and other areas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Profile"
        verbose_name_plural = "Social Profiles"
        ordering = ['platform']

    def __str__(self):
        return f"{self.get_platform_display()} - {self.profile_url}"


class SocialPost(models.Model):
    PLATFORM_CHOICES = [
        ('TIKTOK', 'TikTok'),
        ('INSTAGRAM', 'Instagram'),
        ('YOUTUBE', 'YouTube'),
        ('FACEBOOK', 'Facebook'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField(help_text="Link to the social media post")
    embed_code = models.TextField(blank=True, default="", help_text="Paste the full embed code here (iframe, blockquote, etc.)")
    caption = models.TextField(blank=True, help_text="Optional caption or description")
    is_active = models.BooleanField(default=True, help_text="Show on homepage feed")

    # Additional fields for video details
    title = models.CharField(max_length=500, blank=True, help_text="Title of the video/post")
    author = models.CharField(max_length=200, blank=True, help_text="Author/channel name")
    published_date = models.DateTimeField(blank=True, null=True, help_text="Date published")
    view_count = models.BigIntegerField(default=0, help_text="Number of views")
    like_count = models.BigIntegerField(default=0, help_text="Number of likes")
    comment_count = models.BigIntegerField(default=0, help_text="Number of comments")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_platform_display()} - {self.title or self.created_at.strftime('%Y-%m-%d')}"

    def save(self, *args, **kwargs):
        # Auto-generate embed code if not provided
        if not self.embed_code and self.url:
            generated_embed = generate_embed_code(self.platform, self.url)
            if generated_embed:
                self.embed_code = generated_embed
            else:
                # Ensure embed_code is never null/None
                self.embed_code = ""

        # Fetch additional details for certain platforms
        if self.platform == 'YOUTUBE' and not self.title and self.url:
            self.fetch_youtube_details()

        super().save(*args, **kwargs)

    def fetch_youtube_details(self):
        """Fetch YouTube video details using the API"""
        from .utils import extract_video_id_youtube
        video_id = extract_video_id_youtube(self.url)
        if video_id:
            details = get_youtube_video_details(video_id)
            if details:
                self.title = details.get('title', '')[:500]
                self.author = details.get('channel', '')[:200]
                self.published_date = details.get('published_at')
                self.view_count = int(details.get('view_count', 0))
                self.like_count = int(details.get('like_count', 0))
                self.comment_count = int(details.get('comment_count', 0))

    @property
    def embed_url(self):
        if self.platform == 'YOUTUBE':
            # Handle various YouTube URL formats
            if 'watch?v=' in self.url:
                return self.url.replace('watch?v=', 'embed/').split('&')[0]
            elif 'youtu.be/' in self.url:
                video_id = self.url.split('youtu.be/')[1].split('?')[0]
                return f"https://www.youtube.com/embed/{video_id}"
            elif '/shorts/' in self.url:
                video_id = self.url.split('/shorts/')[1].split('?')[0]
                return f"https://www.youtube.com/embed/{video_id}"
        return self.url
