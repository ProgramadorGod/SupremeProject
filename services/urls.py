from django.urls import path
from services import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Services, name='Services'),
]


