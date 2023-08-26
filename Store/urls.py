from django.urls import path
from Store import views

urlpatterns = [
    path('', views.Store, name='Store'),
]


