from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'home.html')

def products(request):
    return render(request,'products.html')

def contact(request):

    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        msgbox=request.POST['msgbox']

        send_mail(
            email + " - " + name,
            msgbox,
            email,
            ['rishiganapathi07@gmail.com'],
            fail_silently=False
        )    

    return render(request,'contact.html')
