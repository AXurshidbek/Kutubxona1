"""
URL configuration for Kutubxona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from kutubxonaapp.views import *

urlpatterns = [
    path('boshqaruvchi/', admin.site.urls),
    path('salom/', salomlashish),
    path('', homepage),
    path('kitoblar/', kitoblar),
    path('Alisher_Navoiy_kitoblari/', Alisher_Navoiy_kitoblari),
    path('kitob/<int:son>', kitob),
    path('talabalar/', talabalar),
    path('mualliflar/', mualliflar),
    path('talaba_ochir/<int:son>', talaba_ochir),
    path('kitob_ochir/<int:son>', kitob_ochir),


]
