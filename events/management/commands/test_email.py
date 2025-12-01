from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Test email delivery to christianokwena@gmail.com'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            default='christianokwena@gmail.com',
            help='Email address to send test to (default: christianokwena@gmail.com)',
        )

    def handle(self, *args, **options):
        email_address = options['email']
        
        try:
            # Send a test email
            result = send_mail(
                subject='Test Email from Mkenya Isaak 7 Million',
                message='This is a test email to verify that email delivery is working properly.',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@mkenyaisaak.com'),
                recipient_list=[email_address],
                fail_silently=False,
            )
            
            if result:
                self.stdout.write(
                    self.style.SUCCESS(f'Test email sent successfully to {email_address}')
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to send email to {email_address}')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error sending email: {str(e)}')
            )
            
        # Also print the current email settings for debugging
        self.stdout.write(f'DEFAULT_FROM_EMAIL: {getattr(settings, "DEFAULT_FROM_EMAIL", "Not set")}')
        self.stdout.write(f'EMAIL_BACKEND: {getattr(settings, "EMAIL_BACKEND", "Not set")}')
        self.stdout.write(f'SERVER_EMAIL: {getattr(settings, "SERVER_EMAIL", "Not set")}')