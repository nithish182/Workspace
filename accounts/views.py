from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# Create your views here.
def register(request):

    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!')
                return redirect('register')

            else:    
                user = User.objects.create_user(first_name=fullname, username=username, password=password1)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'Password does not match!')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


