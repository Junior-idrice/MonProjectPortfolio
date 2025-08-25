from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'folio/index.html')
def layout(request):
    return render(request,'folio/layout.html')