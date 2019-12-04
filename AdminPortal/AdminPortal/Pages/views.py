from django.shortcuts import render, redirect

# Create your views here.
def globalPage(request):
    return render(request, 'Pages/global.html')

def finPage(request):
    return render(request, 'Pages/Finance.html')

def salPage(request):
    return render(request, 'Pages/Sales.html')

def HRPage(request):
    return render(request, 'Pages/HR.html')

def EngineerPage(request):
    return render(request, 'Pages/Engineer.html')

def red(request):
    return render(request, 'Pages/Redirect.html')

def user(request):
    return render(request, 'Pages/User.html')