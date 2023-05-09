from django.contrib import admin
from .models import Vyrobce, Auto, Autobazar, Zamestnanec

# Register your models here.
admin.site.register(Vyrobce)
admin.site.register(Auto)
admin.site.register(Autobazar)
admin.site.register(Zamestnanec)