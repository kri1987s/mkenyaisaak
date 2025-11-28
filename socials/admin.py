from django.contrib import admin
from django.db import models
from django import forms
from .models import SocialPost, SocialProfile, SocialMediaChannel


class SocialPostAdminForm(forms.ModelForm):
    class Meta:
        model = SocialPost
        fields = '__all__'
        widgets = {
            'embed_code': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
            'caption': forms.Textarea(attrs={'rows': 3}),
        }


@admin.register(SocialMediaChannel)
class SocialMediaChannelAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_name', 'channel_identifier', 'is_active', 'last_sync', 'created_at')
    list_filter = ('platform', 'is_active', 'created_at')
    search_fields = ('channel_identifier', 'display_name', 'channel_url')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at', 'last_sync')
    fieldsets = (
        (None, {
            'fields': ('platform', 'channel_url', 'channel_identifier', 'display_name', 'is_active')
        }),
        ('Sync Information', {
            'fields': ('last_sync',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    help_texts = {
        'channel_url': 'Enter the URL to the social media channel/profile',
        'channel_identifier': 'Unique identifier for the channel (e.g., username, ID)',
        'last_sync': 'When the feed was last synced automatically',
    }


@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_name', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('display_name', 'profile_url')
    list_editable = ('is_active',)


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    form = SocialPostAdminForm
    list_display = ('platform', 'title_preview', 'author', 'created_at', 'is_active')
    list_filter = ('platform', 'is_active', 'created_at')
    search_fields = ('caption', 'title', 'url', 'author')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at', 'embed_code', 'title', 'author',
                      'published_date', 'view_count', 'like_count', 'comment_count')
    fieldsets = (
        (None, {
            'fields': ('platform', 'url', 'caption', 'is_active')
        }),
        ('Video/Post Details', {
            'fields': ('title', 'author', 'published_date', 'view_count', 'like_count', 'comment_count'),
            'classes': ('collapse',)
        }),
        ('Embed Information', {
            'fields': ('embed_code',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    help_texts = {
        'url': 'Enter the URL to the social media post. The embed code and details will be auto-generated.',
        'embed_code': 'The embed code is automatically generated from the URL. You can override it if needed.',
        'title': 'Title is automatically fetched for YouTube videos.',
        'author': 'Author/Channel name is automatically fetched for YouTube videos.',
    }

    def title_preview(self, obj):
        return obj.title[:50] + '...' if obj.title else obj.caption[:50] + '...' if obj.caption else '-'
    title_preview.short_description = 'Title/Caption'