from django.urls import path
from ShoppingCart import views



app_name = "ShoppingCart"

urlpatterns = [
    path("AddProduct/<int:product_Id>/", views.AddProduct, name="AddProduct"),
    path("SubtractPds/<int:product_Id>/", views.Subtract, name="SubstractPds"),
    path("Delete/<int:product_Id>/", views.DeleteProduct, name="Delete"),
    path("Clean/", views.Clean, name="Clean"),

]



