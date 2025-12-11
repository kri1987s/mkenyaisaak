from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

class Command(BaseCommand):
    help = 'Sends a test HTML email to a specified recipient.'

    def add_arguments(self, parser):
        parser.add_argument('recipient_email', type=str, help='The email address to send the test email to.')

    def handle(self, *args, **options):
        recipient_email = options['recipient_email']
        self.stdout.write(f"Attempting to send a test HTML email to {recipient_email}...")

        subject = "Test HTML Email from Django"
        
        # Simple HTML content
        html_content = render_to_string('test_email_template.html', {'message': 'This is a <strong>test</strong> message with a <a href="https://example.com">link</a> and a <button style="background-color: #0d6efd; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; display: inline-block;">Button</button>.'})
        
        # Create plain text version
        text_content = strip_tags(html_content)

        try:
            msg = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient_email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            self.stdout.write(self.style.SUCCESS(f"Successfully sent test HTML email to {recipient_email}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to send test HTML email: {e}"))
