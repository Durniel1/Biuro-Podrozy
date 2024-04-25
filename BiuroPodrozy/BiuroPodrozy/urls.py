"""
URL configuration for BiuroPodrozy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import SrodekTransportuList,SrodekTransportuDetail,SrodekTransportuAddView,KierunekList,KierunekDetail,BiletList,BiletDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('SrodkiTransportu', SrodekTransportuList.as_view(), name="SrodkiTransportu"),
    path('SrodkiTransportu/<int:pk>', SrodekTransportuDetail.as_view(), name="SrodekTransportu"),
    path('SrodkiTransportu/Dodaj', SrodekTransportuAddView, name="DodajSrodekTransportu"),
    
    path('Kierunki', KierunekList.as_view(), name="Kierunki"),
    path('Kierunki/<int:pk>', KierunekDetail.as_view(), name="Kierunek"),
    
    path('Bilety', BiletList.as_view(), name="Bilety"),
    path('Bilety/<int:pk>', BiletDetail.as_view(), name="Bilet"),
    
]
