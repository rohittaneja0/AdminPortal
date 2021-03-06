"""AdminPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from users import views as user_views
from Pages import views as page_views
from django.contrib.auth import views as auth_views

from Portal.views import index, user_login, user_logout, success

urlpatterns = [
    path('',index,name='home'),
    path('Portal/', include('Portal.urls')),
    path('accounts/',include('accounts.urls')),
    #path('', include("django.contrib.auth.urls")),
    #path('accounts/', auth_views.Login.as_view()(template_name='Portal/login.html'),name='login'),
    path('admin/', admin.site.urls),
    path('Pages/', page_views.globalPage,name='global'),
    path('register/', user_views.register, name='register'),
    path('finance/',page_views.finPage, name='finance'),
    path('sales/',page_views.salPage,name='sales'),
    path('hr/',page_views.HRPage,name='HR'),
    path('engineer/',page_views.EngineerPage,name='Engineer'),
    path('redirect/',page_views.red,name='Redirect'),
    path('users/',page_views.user,name='User'),
    


    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()