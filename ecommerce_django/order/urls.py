from django.urls import path
from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('paypal-create-payment/', views.create_paypal_payment),
    path('paypal-execute-payment/', views.execute_paypal_payment),
    path('orders/', views.OrdersList.as_view()),
]