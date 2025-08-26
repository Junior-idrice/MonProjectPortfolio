from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        form = Contact(name=name, email=email, text=text)
        form.save()
        messages.success(request, "message send")
    return render(request, 'folio/index.html')
def layout(request):
    return render(request,'folio/layout.html')

def experience(request):
    return render(request, 'folio/experience.html')

def awards(request):
    return render(request, 'folio/awards.html')

