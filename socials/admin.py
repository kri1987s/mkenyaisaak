from django.contrib import admin
from .models import SocialPost

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'created_at', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('caption',)
