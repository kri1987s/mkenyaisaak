from socials.models import SocialProfile

def social_profiles_context(request):
    """Context processor to add social profiles to all templates"""
    return {
        'social_profiles': SocialProfile.objects.filter(is_active=True)
    }