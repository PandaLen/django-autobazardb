from django.shortcuts import render

from .models import Auto, Autobazar, Zamestnanec
from django.views.generic import DetailView


def index(request):
    auto = 'auta'
    context = {
        'nadpis': auto,
        'auta': Auto.objects.order_by('-rok_vyroby'),
        'autobazary': Autobazar.objects.all()
    }
    return render(request, 'index.html', context=context)

def auta(request):
    context = {
        'auta': Auto.objects.all(),
    }
    return render(request, 'auta.html', context=context)

def autobazary(request):
    context = {
        'autobazary': Autobazar.objects.all(),
    }
    return render(request, 'autobazary.html', context=context)

def zamestnanci(request):
    context = {
        'zamestnanci': Zamestnanec.objects.all(),
    }
    return render(request, 'zamestnanci.html', context=context)

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'auto/detail.html'
    context_object_name = 'auto'
    
class AutobazarDetailView(DetailView):
    model = Autobazar
    template_name = 'autobazar/detail.html'
    context_object_name = 'autobazar'
    
class ZamestnanecDetailView(DetailView):
    model = Zamestnanec
    template_name = 'zamestnanec/detail.html'
    context_object_name = 'zamestnanec'