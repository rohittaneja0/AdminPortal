from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from Portal.forms import UserForm
from AdminPortal.decorators import admin_only
from django import template
from django.contrib.auth.models import Group


def index(request):
    return HttpResponseRedirect(reverse('employee_list'))

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "registration/login.html", context)
    else:
        return render(request, "registration/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "registration/success.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def employee_list(request):
    print(request.role)
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'Portal/index.html', context)

@login_required(login_url="/login/")
def employee_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'Portal/details.html', context)


@login_required(login_url="/login/")
@admin_only
def employee_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()    
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'Portal/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'Portal/add.html', context)

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

