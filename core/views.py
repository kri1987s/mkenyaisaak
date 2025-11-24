from django.views.generic import TemplateView
from django.utils import timezone
from events.models import Event
from socials.models import SocialPost

class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch upcoming active events
        events = Event.objects.filter(
            is_active=True,
            date__gte=timezone.now()
        ).order_by('date').only('id', 'title', 'description', 'poster', 'date', 'venue')
        
        context['featured_event'] = events.first()
        context['upcoming_events'] = events[1:4] if events.count() > 1 else []
        
        # Fetch active social posts
        context['social_posts'] = SocialPost.objects.filter(
            is_active=True
        ).order_by('-created_at')[:6].only('id', 'platform', 'url', 'caption', 'created_at')
        
        return context
