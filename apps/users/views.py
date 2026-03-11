from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("/")

    return render(request, "login.html")


def logout_view(request):

    logout(request)

    return redirect("/")

@login_required
def profile_view(request):

    return render(request, "profile.html")