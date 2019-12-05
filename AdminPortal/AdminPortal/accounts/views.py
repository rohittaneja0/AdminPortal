from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'Portal/home.html')