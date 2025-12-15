from django import template

register = template.Library()

@register.filter
def format_phone_for_whatsapp(phone_number):
    """
    Formats a phone number to the E.164 format for WhatsApp 'wa.me' links.
    - Strips leading '+'
    - If it starts with '0', it replaces it with '254'
    - If it doesn't start with '254', it prepends '254'
    """
    if not isinstance(phone_number, str):
        return phone_number

    phone_number = phone_number.strip()
    if phone_number.startswith('+'):
        phone_number = phone_number[1:]

    if phone_number.startswith('0'):
        return '254' + phone_number[1:]
    
    if not phone_number.startswith('254'):
        return '254' + phone_number
        
    return phone_number
