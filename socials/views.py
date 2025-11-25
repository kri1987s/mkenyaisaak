from django.shortcuts import render
from django.core.paginator import Paginator
from .models import SocialPost, SocialProfile

def socials_index(request):
    """Display all social posts with pagination"""
    social_posts = SocialPost.objects.filter(is_active=True).order_by('-created_at')
    paginator = Paginator(social_posts, 12)  # Show 12 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get active social profiles for links
    social_profiles = SocialProfile.objects.filter(is_active=True)

    context = {
        'page_obj': page_obj,
        'social_profiles': social_profiles,
    }
    return render(request, 'socials/index.html', context)

def get_social_profiles_context():
    """Helper function to get social profiles for use in other views"""
    return {
        'social_profiles': SocialProfile.objects.filter(is_active=True)
    }
