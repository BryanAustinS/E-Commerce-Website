import paypalrestsdk
from paypalrestsdk import Payment

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "AZX8DPdqiLej8XPDqKMkZugFZ-UbjCP3iCo4Y7Gs_0P0NGK8jUyQkv0bYpnasmCiWsfAI1StyVmRm9PK",
    "client_secret": "EJ1G0n6bqanuVs0s3aJl8-wcsA93EdvmHzZkZTN_NEc-AwtRYbKUwvHfxGpkrnY1QAdfIYI2kzAsCmSO"
})

# Create your views here.
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        paid_amount = sum(
            item.get('quantity') * item.get('product').price
            for item in serializer.validated_data['items']
        )
        # Pass the authenticated user to the serializer
        serializer.save(user=request.user, paid_amount=paid_amount)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_paypal_payment(request):
    order_id = request.data.get('order_id')
    
    try:
        order = Order.objects.get(id=order_id)
        
        payment = Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:8080/cart/success",
                "cancel_url": "http://localhost:8080/cart/checkout"
            },
            "transactions": [{
                "amount": {
                    "total": str(order.paid_amount),
                    "currency": "USD"
                },
                "description": f"Order #{order.id}"
            }]
        })
        
        if payment.create():
            # Extract approval URL
            approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
            order.paypal_payment_id = payment.id
            order.save()
            return Response({"approval_url": approval_url})
        else:
            return Response({"error": payment.error}, status=status.HTTP_400_BAD_REQUEST)
            
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def execute_paypal_payment(request):
    payment_id = request.data.get('paymentID')
    payer_id = request.data.get('payerID')
    
    payment = Payment.find(payment_id)
    
    if payment.execute({"payer_id": payer_id}):
        order = Order.objects.get(paypal_payment_id=payment_id)
        order.paid = True
        order.save()
        return Response({"status": "success"})
    else:
        return Response({"error": payment.error}, status=status.HTTP_400_BAD_REQUEST)