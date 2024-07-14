from django.urls import path
from . import views

app_name = 'demo page'

urlpatterns = [
    path('', views.index, name='home'),
    path('get-weather/<str:city>/', views.get_weather, name='get-weather')
]
