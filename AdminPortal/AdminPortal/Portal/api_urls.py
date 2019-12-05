from django.urls import path, include
from Portal.views import *


urlpatterns = [
    path('employee/', EmployeeListView.as_view())
]