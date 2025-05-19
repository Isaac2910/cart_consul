"""
URL configuration for Cart_consul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from ambassade import views as ambassade_views
from authentification import views as auth_views


urlpatterns = [
    path('', ambassade_views.accueil),         # Vue d'accueil de l'ambassade
    path('login/', auth_views.login_page),     # Vue de login
    path("cartes/", include("ambassade.urls")),
    path('admin/', admin.site.urls),


]


