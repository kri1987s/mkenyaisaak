from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .utils import MpesaClient

def initiate_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        
        # Basic validation
        if not phone_number or not amount:
            return JsonResponse({'error': 'Phone number and amount are required'}, status=400)
            
        # Format phone number if necessary (ensure it starts with 254)
        if phone_number.startswith('0'):
            phone_number = '254' + phone_number[1:]
        elif phone_number.startswith('+254'):
            phone_number = phone_number[1:]
            
        client = MpesaClient()
        # In production, use a real domain for callback
        callback_url = request.build_absolute_uri('/mpesa/callback/')
        
        account_reference = "MkenyaIsaak" # Or dynamic reference
        transaction_desc = "Payment for Services"
        
        response = client.make_stk_push(
            phone_number=phone_number,
            amount=amount,
            account_reference=account_reference,
            transaction_desc=transaction_desc,
            callback_url=callback_url
        )
        
        return render(request, 'mpesa/result.html', {
            'response': response,
            'phone_number': phone_number
        })
        
    return render(request, 'mpesa/initiate.html')

@csrf_exempt
@require_http_methods(["POST"])
def mpesa_callback(request):
    try:
        data = json.loads(request.body)
        # Log the callback data
        print(f"M-Pesa Callback Data: {json.dumps(data, indent=2)}")
        
        # Process the data
        stk_callback = data.get('Body', {}).get('stkCallback', {})
        result_code = stk_callback.get('ResultCode')
        checkout_request_id = stk_callback.get('CheckoutRequestID')
        
        if checkout_request_id:
            from events.models import Booking
            try:
                booking = Booking.objects.get(payment_reference=checkout_request_id)
                
                if result_code == 0:
                    booking.payment_status = 'PAID'
                    booking.save()
                    print(f"Booking {booking.id} marked as PAID.")
                else:
                    booking.payment_status = 'FAILED'
                    booking.save()
                    print(f"Booking {booking.id} marked as FAILED. Reason: {stk_callback.get('ResultDesc')}")
                    
            except Booking.DoesNotExist:
                print(f"Booking with CheckoutRequestID {checkout_request_id} not found.")
            
        return JsonResponse({"result": "ok"})
    except Exception as e:
        print(f"Error processing callback: {e}")
        return JsonResponse({"error": str(e)}, status=500)
