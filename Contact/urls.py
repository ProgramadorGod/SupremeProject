from django.urls import path
from Contact import views

urlpatterns=[
    path('', views.Contact, name='Contact'),
]
