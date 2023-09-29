from django.urls import path
from ShoppingCart import views



app_name = "ShoppingCart"

urlpatterns = [
    path("AddProduct/<int:Product_Id>/", views.AddProduct, name="AddProduct"),
    path("Subtract/<int:Product_Id>/", views.Subtract, name="Substract"),
    path("Delete/<int:Product_Id>/", views.DeleteProduct, name="Delete"),
    path("Clean/", views.Clean, name="Clean"),

]



