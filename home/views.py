from django.shortcuts import render

def base1(request):
    return render(request, "base1.html")

def home(request):
    return render(request, "home/index.html")

def services(request):
    return render(request, "home/services.html")

def services_details(request):
    return render(request, "home/services_details.html")

def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")

def team(request):
    return render(request, "home/team.html")
