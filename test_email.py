#!/usr/bin/env python
"""
Email test script for Mkenya Isaak 7 Million
This script will test if the email system is properly configured
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
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def test_email():
    """Test if email sending is working"""
    print("Testing email functionality...")
    
    try:
        # Send a test email
        subject = 'Test Email - Mkenya Isaak 7 Million'
        html_message = """
        <html>
            <body>
                <h2>Email Test</h2>
                <p>This is a test email to confirm that the email system is working properly for Mkenya Isaak 7 Million.</p>
                <p>If you received this email, your email configuration is set up correctly!</p>
                <p>Best regards,<br>The Mkenya Isaak 7 Million Team</p>
            </body>
        </html>
        """
        plain_message = strip_tags(html_message)
        
        # Send the email
        result = send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['christianokwena@gmail.com'],
            html_message=html_message,
            fail_silently=False,
        )
        
        if result:
            print("✅ Email sent successfully!")
            print(f"Email sent to: christianokwena@gmail.com")
            print(f"From: {settings.DEFAULT_FROM_EMAIL}")
            print(f"Subject: {subject}")
        else:
            print("❌ Email was not sent (unknown error)")
            
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        print("This could be due to:")
        print("- Incorrect SMTP settings")
        print("- Network connectivity issues")
        print("- Incorrect credentials in .env file")
        print("- Email limits/restrictions from the provider")

if __name__ == "__main__":
    test_email()