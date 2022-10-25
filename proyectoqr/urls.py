"""proyectoqr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.conf.urls import url
from django.urls import path, include

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from apps.equipo.views import home, Inicio
from apps.usuariof.views import Login, logoutUsuario
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("equipo/", include(("apps.equipo.urls","equipo"))),
    path("index", login_required(Inicio.as_view()), name="index"),
    path("test", Inicio.as_view(), name="test"),
    path('accounts/login/', Login.as_view(), name='login'),
    path("logout/", login_required(logoutUsuario), name="logout")
]
