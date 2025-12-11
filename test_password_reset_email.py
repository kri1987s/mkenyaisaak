#!/usr/bin/env python
"""
Test the password reset email functionality specifically
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
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def test_password_reset_email():
    """Test password reset email specifically"""
    print("Testing password reset email functionality...")
    
    try:
        User = get_user_model()
        # Try to get an existing user or create a test user
        # For this test, we'll use a placeholder
        test_email = 'christianokwena@gmail.com'
        
        # Create a mock context similar to what Django's password reset uses
        # For this test, we'll use placeholders
        context = {
            'email': test_email,
            'domain': 'mkenyaisaak.co.ke',
            'site_name': 'Mkenya Isaak 7 Million',
            'uid': 'testuid',
            'user': type('obj', (object,), {'pk': 1, 'username': 'testuser'})(),  # Mock user
            'token': default_token_generator.make_token(type('obj', (object,), {'pk': 1})()),
            'protocol': 'https',
        }
        
        # Load the HTML template
        html_email = render_to_string('users/password_reset_email.html', context)
        text_email = strip_tags(html_email)
        
        subject = 'Test: Reset your Mkenya Isaak 7 Million password'
        
        # Send as multipart email
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_email,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[test_email],
        )
        msg.attach_alternative(html_email, "text/html")
        
        result = msg.send()
        
        if result:
            print("✅ Password reset test email sent successfully!")
            print(f"Email sent to: {test_email}")
            print(f"From: {settings.DEFAULT_FROM_EMAIL}")
            print(f"Subject: {subject}")
        else:
            print("❌ Password reset test email was not sent")
            
    except Exception as e:
        print(f"❌ Error sending password reset test email: {str(e)}")

if __name__ == "__main__":
    test_password_reset_email()