from django.urls import path
from Blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Blog, name='Blog'),
]

