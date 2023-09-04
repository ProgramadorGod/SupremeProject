from django.urls import path
from ShoppingCart import views


app_name = "ShoppingCart"

urlpatterns = [
    path("AddProduct/<int:Product_Id>/", views.AddProduct, name="Adding"),
    path("SubtractPds/<int:Product_Id>/", views.Subtract, name="Substracting"),
    path("Delete/<int:Product_Id>/", views.DeleteProduct, name="Deleting"),
    path("Clean/", views.Clean, name="Cleaning"),

]



