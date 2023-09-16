from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.http import HttpResponseBadRequest

# Diccionario para realizar un seguimiento de los intentos de envío por IP
ip_submission_count = {}

def Contact(request):
    ContactFormulary = ContactForm()
    if request.method == "POST":
        # Obtiene la dirección IP del usuario
        user_ip = request.META.get('REMOTE_ADDR', None)

        # Verifica si se han excedido los intentos de envío desde la misma IP
        if ip_submission_count.get(user_ip, 0) >= 200:
            return HttpResponseBadRequest("Has excedido el límite de envíos de formulario desde esta dirección IP.")

        ContactFormulary = ContactForm(data=request.POST)
        if ContactFormulary.is_valid():
            Name = request.POST.get("Name")
            Email = request.POST.get("Email")
            Subject = request.POST.get("Subject")
            Content = request.POST.get("Content")

            # Incrementa el contador de envíos por IP
            ip_submission_count[user_ip] = ip_submission_count.get(user_ip, 0) + 1

            email = EmailMessage(Subject, Content, "pipenet12@gmail.com",[Email])
            try:    
                email.send()
                return redirect("/Contact/?Valid")
            except:
                return redirect("/Contact/?NOTValid")


    return render(request, 'Contact/Contact.html', {'ContactForm': ContactFormulary})
