from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import Booking


@require_http_methods(["GET"])
def check_payment_status(request, booking_id):
    """
    API endpoint to check payment status by booking ID
    """
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        
        return JsonResponse({
            'status': 'success',
            'payment_status': booking.payment_status,
            'payment_reference': booking.payment_reference,
            'mpesa_receipt_number': booking.mpesa_receipt_number,
            'total_amount': str(booking.total_amount),
            'updated_at': booking.updated_at.isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@require_http_methods(["GET"])
def check_payment_status_by_reference(request):
    """
    API endpoint to check payment status by payment reference (CheckoutRequestID)
    Useful for when users only have the original reference ID
    """
    payment_reference = request.GET.get('ref', None)
    
    if not payment_reference:
        return JsonResponse({
            'status': 'error',
            'message': 'Payment reference is required'
        }, status=400)
    
    try:
        booking = get_object_or_404(Booking, payment_reference=payment_reference)
        
        return JsonResponse({
            'status': 'success',
            'booking_id': str(booking.id),
            'payment_status': booking.payment_status,
            'payment_reference': booking.payment_reference,
            'mpesa_receipt_number': booking.mpesa_receipt_number,
            'total_amount': str(booking.total_amount),
            'updated_at': booking.updated_at.isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)