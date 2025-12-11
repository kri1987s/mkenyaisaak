#!/usr/bin/env python
"""
Test the actual password reset email functionality with the custom implementation
"""
import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.append('/home/christiano/www/mkenyaisaak')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mkenyaisaak.settings')

# Configure Django
django.setup()

# Now we can use Django functionality
from users.views import CustomPasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.template import Context

def test_custom_password_reset_email():
    """Test the custom password reset email functionality"""
    print("Testing custom password reset email sending...")
    
    try:
        # Create a mock request object and context similar to what Django would use
        from django.http import HttpRequest
        
        # Since we can't simulate a real request easily, let's test the method directly
        view = CustomPasswordResetView()
        
        # Mock context that would be passed to send_mail
        context = {
            'domain': 'mkenyaisaak.co.ke',
            'site_name': 'Mkenya Isaak 7 Million',
            'uid': 'Mg',  # This would be generated from user ID
            'token': 'test-token',  # This would be generated from token generator
            'user': type('obj', (object,), {'pk': 1})(),  # Mock user object
            'protocol': 'https',
        }
        
        # Test the send_mail method with our custom implementation
        subject_template = 'users/password_reset_subject.txt'
        email_template = 'users/password_reset_email.html'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = 'christianokwena@gmail.com'
        
        view.send_mail(
            subject_template_name=subject_template,
            email_template_name=email_template,
            context=context,
            from_email=from_email,
            to_email=to_email
        )
        
        print("✅ Custom password reset email sent successfully!")
        print(f"Email sent to: {to_email}")
        print(f"From: {from_email}")
        print("The email should now render properly with HTML formatting.")
        
    except Exception as e:
        print(f"❌ Error sending custom password reset email: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_custom_password_reset_email()