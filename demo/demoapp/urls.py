from django.urls import path
from . import views

app_name = 'demo page'

urlpatterns = [
    path('', views.index, name='home'),
]
