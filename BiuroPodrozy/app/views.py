from django.shortcuts import render, redirect
from .models import SrodekTransportu, Kierunek, Bilet, Opinia
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from .forms import SrodekTransportuAddForm

# Create your views here.

class SrodekTransportuList(ListView):
    model = SrodekTransportu
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(SrodekTransportuList, self).get_queryset(*args, **kwargs)
        queryset = queryset.order_by('-przewoznik')
        return queryset

class SrodekTransportuDetail(DetailView):
    model = SrodekTransportu
    context_object_name = "SrodekTransportu"
    
def SrodekTransportuAddView(request):
    if(request.method == 'POST'):
        form = SrodekTransportuAddForm(request.POST)
        if form.is_valid():
            #form.save()
            srodektransportu = SrodekTransportu(nazwa = form.clean_nazwa(), typ = form.clean_typ(), droga_przewozu = form.clean_droga_przewozu(), przewoznik = form.clean_przewoznik())
            srodektransportu.save()
            return redirect('SrodkiTransportu')
    else:
        form = SrodekTransportuAddForm()
    return render(request, 'app/DodajSrodekTransportu.html', context={'form': form})

class KierunekList(ListView):
    model = Kierunek
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(KierunekList, self).get_queryset(*args, **kwargs)
        return queryset

class KierunekDetail(DetailView):
    model = Kierunek
    context_object_name = "Kierunek"
    
class BiletList(ListView):
    model = Bilet
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(BiletList, self).get_queryset(*args, **kwargs)
        queryset = queryset.order_by('-godzina_z')
        return queryset
    
class BiletDetail(DetailView):
    model = Bilet
    context_object_name = "Bilet"