from django.urls import path, include 

from product import views

urlpatterns = [
    # Define the routes and display the output of the views
    path('latest-products/', views.LatestProductsList.as_view()), 
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]