from django.shortcuts import render, redirect

# Create your views here.
def globalPage(request):
    return render(request, 'Pages/global.html')

def finPage(request):
    return render(request, 'Pages/Finance.html')