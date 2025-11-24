from django.db import models

class SocialPost(models.Model):
    PLATFORM_CHOICES = [
        ('TIKTOK', 'TikTok'),
        ('INSTAGRAM', 'Instagram'),
        ('YOUTUBE', 'YouTube'),
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
