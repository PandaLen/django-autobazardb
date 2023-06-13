from django.shortcuts import render

from .models import Auto, Autobazar


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