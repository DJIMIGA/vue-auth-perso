from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import CustomUser
from accounts.forms import UserRegistrationsForm


def home(request):
    return HttpResponse("Acueil du site")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationsForm()

    return render(request, "accounts/vue-auth-perso.html", {"form": form})
