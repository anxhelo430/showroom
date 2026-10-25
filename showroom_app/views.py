from django.shortcuts import render


def home(request):
    return render(request, "showroom_app/home.html")


def about(request):
    return render(request, "showroom_app/about.html")


def contact(request):
    return render(request, "showroom_app/contact.html")


def models_page(request):
    return render(request, "showroom_app/models.html")