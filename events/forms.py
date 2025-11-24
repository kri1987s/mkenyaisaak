from django import forms
from .models import TicketType

class BookingForm(forms.Form):
    customer_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    customer_phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0712345678'}))
    
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        super().__init__(*args, **kwargs)
        
        # Dynamically add fields for each ticket type
        for ticket_type in event.ticket_types.all():
            field_name = f"ticket_{ticket_type.id}"
            self.fields[field_name] = forms.IntegerField(
                label=f"{ticket_type.name} (KES {ticket_type.price})",
                min_value=0,
                max_value=10, # Limit max tickets per booking
                initial=0,
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )

    def clean(self):
        cleaned_data = super().clean()
        total_tickets = 0
        for name, value in cleaned_data.items():
            if name.startswith('ticket_'):
                total_tickets += value
        
        if total_tickets == 0:
            raise forms.ValidationError("Please select at least one ticket.")
        return cleaned_data
