from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('auta', views.auta, name='auta'),
]
