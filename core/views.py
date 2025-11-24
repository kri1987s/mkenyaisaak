from django.views.generic import TemplateView
from django.utils import timezone
from events.models import Event
from socials.models import SocialPost

class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch upcoming active events
        context['upcoming_events'] = Event.objects.filter(
            is_active=True,
            date__gte=timezone.now()
        ).order_by('date')[:3]
        
        # Fetch active social posts
        context['social_posts'] = SocialPost.objects.filter(
            is_active=True
        ).order_by('-created_at')[:10]
        
        return context
