from django.urls import path
from SupremeApp import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Store/', views.Store, name='Store'),
    path('Blog/', views.Blog, name='Blog'),
    path('Contact/', views.Contact, name='Contact'),
]


