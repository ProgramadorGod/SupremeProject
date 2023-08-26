from django.urls import path
from SupremeApp import views

urlpatterns = [
    path('', views.Home, name='Home'),

    path('Contact/', views.Contact, name='Contact'),
]


