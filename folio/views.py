from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        message = f"From: {name}\nEmail: {email}\n\nMessage:\n{text}"
        form = Contact(name=name, email=email, text=text)
        

        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['idrice@gmail.com'],  
        )
        return redirect('index') 


       
       
    return render(request, 'folio/index.html')
def layout(request):
    return render(request,'folio/layout.html')

def experience(request):
    return render(request, 'folio/experience.html')

def awards(request):
    return render(request, 'folio/awards.html')

