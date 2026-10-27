from django.shortcuts import render
from .models import*

def home(request):
    allcars = cars.objects.all()
    context = {"allcars":allcars}
    return render(request, "showroom_app/home.html" , context)
    



def about(request):
    return render(request, "showroom_app/about.html")


def contact(request):
    return render(request, "showroom_app/contact.html")


def models_page(request):
    return render(request, "showroom_app/models.html")