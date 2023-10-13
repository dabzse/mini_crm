from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# from django.contrib.auth.models import User
from .forms import RegisterForm, AddCustomerForm
from .models import Customer


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect("home")
        else:
            messages.warning(request, ("Error logging in - Please try again..."))
            return redirect("home")


    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
            Q(username__icontains=q) |
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(email__icontains=q)
        )
        customers = Customer.objects.filter(multiple_q)

    else:
        customers = Customer.objects.all()

    records_per_page = 20
    paginator = Paginator(customers, records_per_page)
    page = request.GET.get("page")
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        customers = paginator.page(paginator.num_pages)

    context = {
        "count": paginator.count,
        "customers": customers,
    }

    return render(request, "home.html", context)


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


def customer_data(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        return render(request, "customer.html", {"customer": customer})
    else:
        messages.warning(request, ("Please login first..."))
        return redirect("home")


def del_cst(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        messages.success(request, ("Customer has been deleted!"))
        return redirect("home")
    else:
        messages.warning(request, ("Please login first..."))
        return redirect("home")


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, ("Customer has been added!"))
                return redirect("home")
        return render(request, "add_customer.html", {"form": form})
    else:
        messages.warning(request, ("Please login first..."))
        return redirect("home")


def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, ("Customer has been updated!"))
            return redirect("home")
        return render(request, "update_customer.html", {"form": form})
    else:
        messages.warning(request, ("Please login first..."))
        return redirect("home")
