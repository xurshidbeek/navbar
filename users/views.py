from django.shortcuts import render


def login(request):
    return render(request, "auther/login.html")


def register(request):
    return render(request, "auther/register.html")

# Create your views here.
