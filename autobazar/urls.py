from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('auta', views.auta, name='auta'),
    path('auta/<int:pk>', views.AutoDetailView.as_view(), name='auto_detail'),
    path('autobazary', views.autobazary, name='autobazary'),
    path('autobazary/<int:pk>', views.AutobazarDetailView.as_view(), name='autobazar_detail'),
    path('zamestnanci', views.zamestnanci, name='zamestnanci'),
    path('zamestnanci/<int:pk>', views.ZamestnanecDetailView.as_view(), name='zamestnanec_detail'),
]
