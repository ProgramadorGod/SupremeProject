from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.


class VRegister(View):
    def get(self, request):
        return render(request,'authentication/register.html')
        #form = UserCreationForm()
        #return render(request,'authentication/register.html', {"form":form})

    def post(self, request):
        user_name = request.POST.get("user")
        password = request.POST.get("password")
        user = User.objects.filter(username=user_name).first()


        if user:
            if check_password(password, user.password):
                return HttpResponse("Autenticated!!!")
            
            return HttpResponse("Invalid password.")

        return HttpResponse("User not found")