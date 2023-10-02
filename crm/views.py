from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect("home")
        else:
            messages.warning(request, ("Error logging in - Please try again..."))
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.info(request, ("You have been logged out!"))
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Get form values
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # Authenticate user
            user = authenticate(username=username, password=password)
            # Login user
            login(request, user)
            messages.success(request, ("You have been registered!"))
            return redirect("home")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


'''
        # Get form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        # Check if passwords match
        if password == password_confirm:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.warning(request, ("That username is already taken!"))
                return render(request, "register.html", {})
            elif User.objects.filter(email=email).exists():
                messages.warning(request, ("That email is already being used!"))
                return render(request, "register.html", {})
            else:
                # Looks good
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                # Login after register
                # auth.login(request, user)
                # messages.success(request, ("You have been logged in!"))
                # return redirect("home")
                user.save()
                messages.success(request, ("You have been registered!"))
                return render(request, "login.html", {})
        else:
            messages.error(request, ("Passwords do not match!"))
            return render(request, "register.html", {})
    else:
        return render(request, "register.html", {})

'''