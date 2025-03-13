from django.urls import path, include 

from product import views

urlpatterns = [
    # Define the routes and display the output of the views
    path('latest-products/', views.LatestProductsList.as_view()), 
]