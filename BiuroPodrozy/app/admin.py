from django.contrib import admin
from .models import SrodekTransportu,Bilet,Kierunek,Opinia

# Register your models here.

admin.site.register(SrodekTransportu)
admin.site.register(Bilet)
admin.site.register(Kierunek)
admin.site.register(Opinia)