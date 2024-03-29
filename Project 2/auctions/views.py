from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Product

def new(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        image_url = request.POST["image_url"]
        price = request.POST["price"]
        category = request.POST["category"]
        owner = request.user
        new_product = Product(
            title=title,
            description=description,
            image_url=image_url,
            price=price,
            category=Category.objects.get(category_name=category),
            owner=owner
        )
        new_product.save()
        return HttpResponseRedirect(reverse(index))
    return render(request, "auctions/new.html", {
        "categories": Category.objects.all()
    })

def index(request):
    return render(request, "auctions/index.html", {
        "listings":Product.objects.all(),
        "categories": Category.objects.all()
    })

def listing(request, id):
    data = Product.objects.get(pk=id)
    return render(request, "auctions/listing.html", {
        "data": data
    })

def category(request):
    if request.method == 'POST':
        category = request.POST["category"]
        if category == "all":
            category = Product.objects.all()
        else:
            category = Product.objects.filter(category=Category.objects.get(category_name=category))
        return render(request, "auctions/index.html", {
            "listings": category,
            "categories": Category.objects.all()
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
