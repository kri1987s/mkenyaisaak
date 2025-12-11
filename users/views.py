from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('users:password_reset_done')

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a password reset email using Django's send_mail function.
        This follows the same pattern as other working email functionality in the project.
        """
        from django.core.mail import send_mail
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags
        import logging

        # Render the subject
        subject = render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines()).strip()

        # Render HTML email content
        html_email = render_to_string(email_template_name, context)

        # Create plain text version by stripping HTML tags
        text_email = strip_tags(html_email)

        # Log that our custom method is being called
        logging.info(f"CustomPasswordResetView.send_mail called for: {to_email}")
        logging.info(f"HTML email content preview: {html_email[:100]}...")

        # Use Django's send_mail function with html_message parameter
        # This follows the same pattern as the events app
        send_mail(
            subject=subject,
            message=text_email,  # Plain text version
            from_email=from_email,
            recipient_list=[to_email],
            html_message=html_email,  # HTML version
            fail_silently=False,
        )

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the 3 most recent events
        context['recent_events'] = Event.objects.filter(is_active=True).order_by('-date')[:3]
        return context

class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:home')  # Redirect to homepage if already logged in
        return super().dispatch(request, *args, **kwargs)

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'users/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the 3 most recent events
        context['recent_events'] = Event.objects.filter(is_active=True).order_by('-date')[:3]
        return context
