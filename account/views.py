from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                print("email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password1,
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                return redirect('/')

    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        current_user = auth.authenticate(username=username, password=password)
        if current_user is not None:
            auth.login(request, current_user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    else:
        return render(request, "login.html")


def log_out(request):
    auth.logout(request)
    return redirect("/")

def destination(request):

    list = ["Mumbai", "Hydrabad", "Pune", "Banglore"]

    return render(request, "destinations.html" , {"name":list})
