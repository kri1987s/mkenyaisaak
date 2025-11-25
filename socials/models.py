from django.db import models

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
    caption = models.TextField(blank=True, help_text="Optional caption or description")
    is_active = models.BooleanField(default=True, help_text="Show on homepage feed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_platform_display()} - {self.created_at.strftime('%Y-%m-%d')}"
