from django.urls import path
from Portal.views import *

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('<int:id>/details/', employee_details, name="employee_details"),
    path('add/', employee_add, name="employee_add"),
]