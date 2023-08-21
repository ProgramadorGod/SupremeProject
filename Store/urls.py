from django.urls import path
from Store import views


path('', views.Store, name='Store'),
