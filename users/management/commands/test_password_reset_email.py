from django.core.management.base import BaseCommand
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.views import CustomPasswordResetView
from django.http import HttpRequest

class Command(BaseCommand):
    help = 'Test the password reset email using the same path as the actual view'

    def handle(self, *args, **options):
        self.stdout.write('Testing password reset email using actual view path...')
        
        User = get_user_model()
        
        # Try to get the first user in the system for testing
        # If no user exists, we'll create a mock context
        user = User.objects.first()
        
        if user:
            self.stdout.write(f'Using existing user: {user.username}')
            
            # Generate context similar to what PasswordResetView would create
            context = {
                'email': user.email,
                'domain': 'mkenyaisaak.co.ke',  # You can change this to your actual domain
                'site_name': 'Mkenya Isaak 7 Million',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': default_token_generator.make_token(user),
                'protocol': 'https',
            }
        else:
            # Create a mock context
            self.stdout.write('No users found, creating mock context')
            context = {
                'email': 'test@example.com',
                'domain': 'mkenyaisaak.co.ke',
                'site_name': 'Mkenya Isaak 7 Million',
                'uid': 'Mg',  # Base64 encoded user id
                'user': type('obj', (object,), {'pk': 1, 'username': 'testuser'})(),
                'token': 'test-token',
                'protocol': 'https',
            }
        
        # Create an instance of our custom view
        view = CustomPasswordResetView()
        
        # Call the send_mail method using the same parameters as the actual form
        subject_template = 'users/password_reset_subject.txt'
        email_template = 'users/password_reset_email.html'
        from_email = 'welcome@mkenyaisaak.co.ke'  # Use your configured email
        to_email = 'christianokwena@gmail.com'  # Use the test email address
        
        self.stdout.write(f'Sending password reset email to: {to_email}')
        
        try:
            view.send_mail(
                subject_template_name=subject_template,
                email_template_name=email_template,
                context=context,
                from_email=from_email,
                to_email=to_email
            )
            
            self.stdout.write(
                self.style.SUCCESS('Successfully sent password reset email using the actual view method!')
            )
            self.stdout.write('The email should arrive with proper HTML formatting.')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error sending email: {str(e)}')
            )
            import traceback
            traceback.print_exc()