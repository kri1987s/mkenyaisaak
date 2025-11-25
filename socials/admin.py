from django.contrib import admin
from .models import SocialPost, SocialProfile

@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_name', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('display_name', 'profile_url')
    list_editable = ('is_active',)

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'created_at', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('caption',)
    list_editable = ('is_active',)
