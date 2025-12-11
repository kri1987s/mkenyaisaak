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

    def form_valid(self, form):
        import logging
        from django.contrib.auth import get_user_model
        from django.contrib.auth.tokens import default_token_generator
        from django.utils.http import urlsafe_base64_encode
        from django.utils.encoding import force_bytes
        from django.core.mail import send_mail
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags
        import sys

        print("DEBUG: CustomPasswordResetView.form_valid is running!")
        logging.info("CustomPasswordResetView.form_valid: Starting execution")

        # Get the email from the form
        email = form.cleaned_data['email']
        logging.info(f"CustomPasswordResetView.form_valid: Processing email: {email}")

        # Get the associated users
        User = get_user_model()
        active_users = User._default_manager.filter(email__iexact=email, is_active=True)

        for user in active_users:
            # Create context for the email template
            context = {
                'email': email,
                'user': user,
                'domain': self.request.get_host(),
                'site_name': 'Mkenya Isaak 7 Million',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'https' if self.request.is_secure() else 'http',
            }

            # Render subject
            subject = render_to_string(self.subject_template_name, context)
            subject = ''.join(subject.splitlines()).strip()

            # Render HTML email content
            html_email = render_to_string(self.email_template_name, context)

            # Create plain text version by stripping HTML tags
            text_email = strip_tags(html_email)

            logging.info(f"CustomPasswordResetView: Sending HTML email to {email}")
            logging.info(f"HTML email sample: {html_email[:100]}...")

            # Send the email using the same approach as events app
            from django.conf import settings
            from_email_address = getattr(settings, 'DEFAULT_FROM_EMAIL', 'welcome@mkenyaisaak.co.ke')

            send_mail(
                subject=subject,
                message=text_email,  # Plain text version
                from_email=from_email_address,
                recipient_list=[email],
                html_message=html_email,  # HTML version
                fail_silently=False,
            )

            logging.info(f"CustomPasswordResetView: Email sent to {email}")

        # Return the success response without calling parent (to avoid duplicate emails)
        return super().form_valid(form)

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
